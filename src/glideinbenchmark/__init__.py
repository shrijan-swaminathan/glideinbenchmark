# import pkgutil
# import os
# import sys

# __all__ = []
# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(current_dir)
# sys.path.insert(0, parent_dir)

# print(f"Searching in directories: {sys.path}")

# for loader, module_name, is_pkg in  pkgutil.walk_packages(__path__):
#     print(f"Found module: {module_name}")
#     __all__.append(module_name)
#     _module = loader.find_module(module_name).load_module(module_name)
#     globals()[module_name] = _module