from importlib import import_module


def get_class_by_path(name):
    parts = name.split('.')
    return getattr(import_module('.'.join(parts[0:-1])), parts[-1])


def create_list_of_imported_objects(classlist):
    return [get_class_by_path(name)() for name in classlist]