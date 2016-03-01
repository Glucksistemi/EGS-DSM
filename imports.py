def get_object_by_path(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


def create_list_of_imported_objects(classlist):
    return [get_object_by_path(name)() for name in classlist]