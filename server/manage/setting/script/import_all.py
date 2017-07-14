import pkgutil
import inspect

def import_all(path):

    members = []
    glob = {}

    for loader, name, is_pkg in pkgutil.walk_packages(path):
        module = loader.find_module(name).load_module(name)

        for name, value in inspect.getmembers(module):
            if name.startswith('__'):
                continue

            glob[name] = value
            members.append(name)

    return members, glob


# from server.content.catalog import aa
#
# __all__, glob = aa.import_all(__path__)
# globals().update(glob)