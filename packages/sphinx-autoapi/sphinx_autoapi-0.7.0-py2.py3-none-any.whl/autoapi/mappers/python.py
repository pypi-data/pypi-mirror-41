import collections
import copy
import os

import astroid
import sphinx
import sphinx.util.docstrings
import sphinx.util.logging

from .base import PythonMapperBase, SphinxMapperBase
from . import astroid_utils
from ..utils import slugify

try:
    _TEXT_TYPE = unicode
except NameError:
    _TEXT_TYPE = str

LOGGER = sphinx.util.logging.getLogger(__name__)


def _expand_wildcard_placeholder(original_module, originals_map, placeholder):
    """Expand a wildcard placeholder to a sequence of named placeholders.

    :param original_module: The data dictionary of the module
        that the placeholder is imported from.
    :type original_module: dict
    :param originals_map: A map of the names of children under the module
        to their data dictionaries.
    :type originals_map: dict(str, dict)
    :param placeholder: The wildcard placeholder to expand.
    :type placeholder: dict

    :returns: The placeholders that the wildcard placeholder represents.
    :rtype: list(dict)
    """
    originals = originals_map.values()
    if original_module["all"] is not None:
        originals = []
        for name in original_module["all"]:
            if name == "__all__":
                continue

            if name not in originals_map:
                msg = "Invalid __all__ entry {0} in {1}".format(
                    name, original_module["name"]
                )
                LOGGER.warning(msg)
                continue

            originals.append(originals_map[name])

    placeholders = []
    for original in originals:
        new_full_name = placeholder["full_name"].replace("*", original["name"])
        new_original_path = placeholder["original_path"].replace("*", original["name"])
        if "original_path" in original:
            new_original_path = original["original_path"]
        new_placeholder = dict(
            placeholder,
            name=original["name"],
            full_name=new_full_name,
            original_path=new_original_path,
        )
        placeholders.append(new_placeholder)

    return placeholders


def _resolve_module_placeholders(modules, module_name, visit_path, resolved):
    """Resolve all placeholder children under a module.

    :param modules: A mapping of module names to their data dictionary.
        Placeholders are resolved in place.
    :type modules: dict(str, dict)
    :param module_name: The name of the module to resolve.
    :type module_name: str
    :param visit_path: An ordered set of visited module names.
    :type visited: collections.OrderedDict
    :param resolved: A set of already resolved module names.
    :type resolved: set(str)
    """
    if module_name in resolved:
        return

    visit_path[module_name] = True

    module, children = modules[module_name]
    for child in list(children.values()):
        if child["type"] != "placeholder":
            continue

        imported_from, original_name = child["original_path"].rsplit(".", 1)
        if imported_from in visit_path:
            msg = "Cannot resolve cyclic import: {0}, {1}".format(
                ", ".join(visit_path), imported_from
            )
            LOGGER.warning(msg)
            module["children"].remove(child)
            children.pop(child["name"])
            continue

        if imported_from not in modules:
            msg = "Cannot resolve import of unknown module {0} in {1}".format(
                imported_from, module_name
            )
            LOGGER.warning(msg)
            module["children"].remove(child)
            children.pop(child["name"])
            continue

        _resolve_module_placeholders(modules, imported_from, visit_path, resolved)

        if original_name == "*":
            original_module, originals_map = modules[imported_from]

            # Replace the wildcard placeholder
            # with a list of named placeholders.
            new_placeholders = _expand_wildcard_placeholder(
                original_module, originals_map, child
            )
            child_index = module["children"].index(child)
            module["children"][child_index : child_index + 1] = new_placeholders
            children.pop(child["name"])

            for new_placeholder in new_placeholders:
                if new_placeholder["name"] not in children:
                    children[new_placeholder["name"]] = new_placeholder
                original = originals_map[new_placeholder["name"]]
                _resolve_placeholder(new_placeholder, original)
        elif original_name not in modules[imported_from][1]:
            msg = "Cannot resolve import of {0} in {1}".format(
                child["original_path"], module_name
            )
            LOGGER.warning(msg)
            module["children"].remove(child)
            children.pop(child["name"])
            continue
        else:
            original = modules[imported_from][1][original_name]
            _resolve_placeholder(child, original)

    del visit_path[module_name]
    resolved.add(module_name)


def _resolve_placeholder(placeholder, original):
    """Resolve a placeholder to the given original object.

    :param placeholder: The placeholder to resolve, in place.
    :type placeholder: dict
    :param original: The object that the placeholder represents.
    :type original: dict
    """
    new = copy.deepcopy(original)
    # The name remains the same.
    new["name"] = placeholder["name"]
    new["full_name"] = placeholder["full_name"]
    # Record where the placeholder originally came from.
    new["original_path"] = original["full_name"]
    # The source lines for this placeholder do not exist in this file.
    # The keys might not exist if original is a resolved placeholder.
    new.pop("from_line_no", None)
    new.pop("to_line_no", None)

    # Resolve the children
    stack = list(new.get("children", ()))
    while stack:
        child = stack.pop()
        # Relocate the child to the new location
        assert child["full_name"].startswith(original["full_name"])
        suffix = child["full_name"][len(original["full_name"]) :]
        child["full_name"] = new["full_name"] + suffix
        # The source lines for this placeholder do not exist in this file.
        # The keys might not exist if original is a resolved placeholder.
        child.pop("from_line_no", None)
        child.pop("to_line_no", None)
        # Resolve the remaining children
        stack.extend(child.get("children", ()))

    placeholder.clear()
    placeholder.update(new)


class PythonSphinxMapper(SphinxMapperBase):

    """Auto API domain handler for Python

    Parses directly from Python files.

    :param app: Sphinx application passed in as part of the extension
    """

    def load(self, patterns, dirs, ignore=None):
        """Load objects from the filesystem into the ``paths`` dictionary

        Also include an attribute on the object, ``relative_path`` which is the
        shortened, relative path the package/module
        """
        for dir_ in dirs:
            dir_root = dir_
            if os.path.exists(os.path.join(dir_, "__init__.py")):
                dir_root = os.path.abspath(os.path.join(dir_, os.pardir))

            for path in self.find_files(patterns=patterns, dirs=[dir_], ignore=ignore):
                data = self.read_file(path=path)
                if data:
                    data["relative_path"] = os.path.relpath(path, dir_root)
                    self.paths[path] = data

    def read_file(self, path, **kwargs):
        """Read file input into memory, returning deserialized objects

        :param path: Path of file to read
        """
        try:
            parsed_data = Parser().parse_file(path)
            return parsed_data
        except (IOError, TypeError, ImportError):
            LOGGER.warning("Error reading file: {0}".format(path))
        return None

    def _resolve_placeholders(self):
        """Resolve objects that have been imported from elsewhere."""
        modules = {}
        for module in self.paths.values():
            children = {child["name"]: child for child in module["children"]}
            modules[module["name"]] = (module, children)

        resolved = set()
        for module_name in modules:
            visit_path = collections.OrderedDict()
            _resolve_module_placeholders(modules, module_name, visit_path, resolved)

    def map(self, options=None):
        self._resolve_placeholders()

        super(PythonSphinxMapper, self).map(options)

        parents = {obj.name: obj for obj in self.objects.values()}
        for obj in self.objects.values():
            parent_name = obj.name.rsplit(".", 1)[0]
            if parent_name in parents and parent_name != obj.name:
                parent = parents[parent_name]
                attr = "sub{}s".format(obj.type)
                getattr(parent, attr).append(obj)

        for obj in self.objects.values():
            obj.submodules.sort()
            obj.subpackages.sort()

    def create_class(self, data, options=None, **kwargs):
        """Create a class from the passed in data

        :param data: dictionary data of parser output
        """
        obj_map = dict(
            (cls.type, cls)
            for cls in [
                PythonClass,
                PythonFunction,
                PythonModule,
                PythonMethod,
                PythonPackage,
                PythonAttribute,
                PythonData,
                PythonException,
            ]
        )
        try:
            cls = obj_map[data["type"]]
        except KeyError:
            LOGGER.warning("Unknown type: %s" % data["type"])
        else:
            obj = cls(
                data,
                class_content=self.app.config.autoapi_python_class_content,
                options=self.app.config.autoapi_options,
                jinja_env=self.jinja_env,
                url_root=self.url_root,
                **kwargs
            )

            lines = sphinx.util.docstrings.prepare_docstring(obj.docstring)
            if lines and "autodoc-process-docstring" in self.app.events.events:
                self.app.emit(
                    "autodoc-process-docstring",
                    cls.type,
                    obj.name,
                    None,  # object
                    None,  # options
                    lines,
                )
            obj.docstring = "\n".join(lines)

            for child_data in data.get("children", []):
                for child_obj in self.create_class(
                    child_data, options=options, **kwargs
                ):
                    obj.children.append(child_obj)
            yield obj


class PythonPythonMapper(PythonMapperBase):

    language = "python"
    is_callable = False

    def __init__(self, obj, class_content="class", **kwargs):
        super(PythonPythonMapper, self).__init__(obj, **kwargs)

        self.name = obj["name"]
        self.id = obj.get("full_name", self.name)

        # Optional
        self.children = []
        self.args = obj.get("args")
        self.docstring = obj["doc"]

        # For later
        self.item_map = collections.defaultdict(list)
        self._class_content = class_content

    @property
    def args(self):
        return self._args

    @args.setter
    def args(self, value):
        self._args = value

    @property
    def docstring(self):
        return self._docstring

    @docstring.setter
    def docstring(self, value):
        self._docstring = value

    @property
    def is_undoc_member(self):
        return not bool(self.docstring)

    @property
    def is_private_member(self):
        return self.short_name.startswith("_") and not self.short_name.endswith("__")

    @property
    def is_special_member(self):
        return self.short_name.startswith("__") and self.short_name.endswith("__")

    @property
    def display(self):
        if self.is_undoc_member and "undoc-members" not in self.options:
            return False
        if self.is_private_member and "private-members" not in self.options:
            return False
        if self.is_special_member and "special-members" not in self.options:
            return False
        return True

    @property
    def summary(self):
        for line in self.docstring.splitlines():
            line = line.strip()
            if line:
                return line

        return ""

    def _children_of_type(self, type_):
        return list(child for child in self.children if child.type == type_)


class PythonFunction(PythonPythonMapper):
    type = "function"
    is_callable = True
    ref_directive = "func"


class PythonMethod(PythonPythonMapper):
    type = "method"
    is_callable = True
    ref_directive = "meth"

    def __init__(self, obj, **kwargs):
        super(PythonMethod, self).__init__(obj, **kwargs)

        self.method_type = obj["method_type"]

    @property
    def display(self):
        if self.short_name == "__init__":
            return False

        return super(PythonMethod, self).display


class PythonData(PythonPythonMapper):
    """Global, module level data."""

    type = "data"

    def __init__(self, obj, **kwargs):
        super(PythonData, self).__init__(obj, **kwargs)

        self.value = obj.get("value")


class PythonAttribute(PythonData):
    """An object/class level attribute."""

    type = "attribute"


class TopLevelPythonPythonMapper(PythonPythonMapper):
    ref_directive = "mod"
    _RENDER_LOG_LEVEL = "VERBOSE"

    def __init__(self, obj, **kwargs):
        super(TopLevelPythonPythonMapper, self).__init__(obj, **kwargs)

        self.top_level_object = "." not in self.name

        self.subpackages = []
        self.submodules = []
        self.all = obj["all"]

    @property
    def functions(self):
        return self._children_of_type("function")

    @property
    def classes(self):
        return self._children_of_type("class")


class PythonModule(TopLevelPythonPythonMapper):
    type = "module"


class PythonPackage(TopLevelPythonPythonMapper):
    type = "package"


class PythonClass(PythonPythonMapper):
    type = "class"

    def __init__(self, obj, **kwargs):
        super(PythonClass, self).__init__(obj, **kwargs)

        self.bases = obj["bases"]

    @PythonPythonMapper.args.getter
    def args(self):
        args = self._args

        constructor = self.constructor
        if constructor:
            args = constructor.args

        if args.startswith("self"):
            args = args[4:].lstrip(",").lstrip()

        return args

    @PythonPythonMapper.docstring.getter
    def docstring(self):
        docstring = super(PythonClass, self).docstring

        if self._class_content in ("both", "init"):
            constructor_docstring = self.constructor_docstring
            if constructor_docstring:
                if self._class_content == "both":
                    docstring = "{0}\n{1}".format(docstring, constructor_docstring)
                else:
                    docstring = constructor_docstring

        return docstring

    @property
    def methods(self):
        return self._children_of_type("method")

    @property
    def attributes(self):
        return self._children_of_type("attribute")

    @property
    def classes(self):
        return self._children_of_type("class")

    @property
    def constructor(self):
        for child in self.children:
            if child.short_name == "__init__":
                return child

        return None

    @property
    def constructor_docstring(self):
        docstring = ""

        constructor = self.constructor
        if constructor and constructor.docstring:
            docstring = constructor.docstring
        else:
            for child in self.children:
                if child.short_name == "__new__":
                    docstring = child.docstring
                    break

        return docstring


class PythonException(PythonClass):
    type = "exception"


class Parser(object):
    def __init__(self):
        self._name_stack = []
        self._encoding = None

    def _get_full_name(self, name):
        return ".".join(self._name_stack + [name])

    def _encode(self, to_encode):
        if self._encoding:
            try:
                return _TEXT_TYPE(to_encode, self._encoding)
            except TypeError:
                # The string was already in the correct format
                pass

        return to_encode

    def parse_file(self, file_path):
        directory, filename = os.path.split(file_path)
        module_parts = []
        if filename != "__init__.py":
            module_part = os.path.splitext(filename)[0]
            module_parts = [module_part]
        module_parts = collections.deque(module_parts)
        while os.path.isfile(os.path.join(directory, "__init__.py")):
            directory, module_part = os.path.split(directory)
            if module_part:
                module_parts.appendleft(module_part)

        module_name = ".".join(module_parts)
        node = astroid.MANAGER.ast_from_file(file_path, module_name)
        return self.parse(node)

    def parse_assign(self, node):
        doc = ""
        doc_node = node.next_sibling()
        if isinstance(doc_node, astroid.nodes.Expr) and isinstance(
            doc_node.value, astroid.nodes.Const
        ):
            doc = doc_node.value.value

        type_ = "data"
        if isinstance(
            node.scope(), astroid.nodes.ClassDef
        ) or astroid_utils.is_constructor(node.scope()):
            type_ = "attribute"

        assign_value = astroid_utils.get_assign_value(node)
        if not assign_value:
            return []

        target, value = assign_value
        data = {
            "type": type_,
            "name": target,
            "full_name": self._get_full_name(target),
            "doc": self._encode(doc),
            "value": value,
            "from_line_no": node.fromlineno,
            "to_line_no": node.tolineno,
        }

        return [data]

    def parse_classdef(self, node, data=None):
        type_ = "class"
        if astroid_utils.is_exception(node):
            type_ = "exception"

        args = ""
        try:
            constructor = node.lookup("__init__")[1]
        except IndexError:
            pass
        else:
            if isinstance(constructor, astroid.nodes.FunctionDef):
                args = constructor.args.as_string()

        basenames = list(astroid_utils.get_full_basenames(node.bases, node.basenames))

        data = {
            "type": type_,
            "name": node.name,
            "full_name": self._get_full_name(node.name),
            "args": args,
            "bases": basenames,
            "doc": self._encode(node.doc or ""),
            "from_line_no": node.fromlineno,
            "to_line_no": node.tolineno,
            "children": [],
        }

        self._name_stack.append(node.name)
        for child in node.get_children():
            child_data = self.parse(child)
            if child_data:
                data["children"].extend(child_data)
        self._name_stack.pop()

        return [data]

    def _parse_property(self, node):
        data = {
            "type": "attribute",
            "name": node.name,
            "full_name": self._get_full_name(node.name),
            "doc": self._encode(node.doc or ""),
            "from_line_no": node.fromlineno,
            "to_line_no": node.tolineno,
        }

        return [data]

    def parse_functiondef(self, node):
        if astroid_utils.is_decorated_with_property(node):
            return self._parse_property(node)
        if astroid_utils.is_decorated_with_property_setter(node):
            return []

        type_ = "function" if node.type == "function" else "method"

        data = {
            "type": type_,
            "name": node.name,
            "full_name": self._get_full_name(node.name),
            "args": node.args.as_string(),
            "doc": self._encode(node.doc or ""),
            "from_line_no": node.fromlineno,
            "to_line_no": node.tolineno,
        }

        if type_ == "method":
            data["method_type"] = node.type

        result = [data]

        if node.name == "__init__":
            for child in node.get_children():
                if isinstance(child, astroid.Assign):
                    child_data = self.parse_assign(child)
                    result.extend(data for data in child_data if data["doc"])

        return result

    def _parse_local_import_from(self, node):
        result = []

        for name, alias in node.names:
            is_wildcard = (alias or name) == "*"
            full_name = self._get_full_name(alias or name)
            original_path = astroid_utils.get_full_import_name(node, alias or name)

            data = {
                "type": "placeholder",
                "name": original_path if is_wildcard else (alias or name),
                "full_name": full_name,
                "original_path": original_path,
            }
            result.append(data)

        return result

    def parse_module(self, node):
        path = node.path
        if isinstance(node.path, list):
            path = node.path[0] if node.path else None

        type_ = "module"
        if node.package:
            type_ = "package"

        self._name_stack = [node.name]
        self._encoding = node.file_encoding

        data = {
            "type": type_,
            "name": node.name,
            "full_name": node.name,
            "doc": self._encode(node.doc or ""),
            "children": [],
            "file_path": path,
            "encoding": node.file_encoding,
            "all": astroid_utils.get_module_all(node),
        }

        top_name = node.name.split(".", 1)[0]
        for child in node.get_children():
            if node.package and astroid_utils.is_local_import_from(child, top_name):
                child_data = self._parse_local_import_from(child)
            else:
                child_data = self.parse(child)

            if child_data:
                data["children"].extend(child_data)

        return data

    def parse(self, node):
        data = {}

        node_type = node.__class__.__name__.lower()
        parse_func = getattr(self, "parse_" + node_type, None)
        if parse_func:
            data = parse_func(node)
        else:
            for child in node.get_children():
                data = self.parse(child)
                if data:
                    break

        return data
