#!/usr/bin/python3.8

import dis
import importlib.util

if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("hidden_module", "hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    hidden_names = []
    for name in dir(module):
        if not name.startswith("__"):
            hidden_names.append(name)

    hidden_names.sort()

    for name2 in hidden_names:
        print(name2)
