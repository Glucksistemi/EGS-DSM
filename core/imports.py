import sys


def get_class_by_path(name):
    parts = name.split('.')
    print name
    module = import_module('.'.join(parts[0:-1]))
    return getattr(import_module('.'.join(parts[0:-1])), parts[-1])


def create_list_of_imported_objects(classlist):
    return [get_class_by_path(name)() for name in classlist]


def create_dict_of_imported_objects(classdict):
    objdict = {}
    for name, classname in classdict.iteritems():
        objdict[name] = get_class_by_path(classname)()
    return objdict

# Following code was taken from importLib due to some strange problems with importing importlib


def _resolve_name(name, package, level):
    """Return the absolute name of the module to be imported."""
    if not hasattr(package, 'rindex'):
        raise ValueError("'package' not set to a string")
    dot = len(package)
    for x in xrange(level, 1, -1):
        try:
            dot = package.rindex('.', 0, dot)
        except ValueError:
            raise ValueError("attempted relative import beyond top-level "
                              "package")
    return "%s.%s" % (package[:dot], name)


def import_module(name, package=None):
    """Import a module.

    The 'package' argument is required when performing a relative import. It
    specifies the package to use as the anchor point from which to resolve the
    relative import to an absolute import.

    """
    if name.startswith('.'):
        if not package:
            raise TypeError("relative imports require the 'package' argument")
        level = 0
        for character in name:
            if character != '.':
                break
            level += 1
        name = _resolve_name(name[level:], package, level)
    __import__(name)
    return sys.modules[name]
