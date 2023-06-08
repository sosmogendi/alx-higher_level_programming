#!/usr/bin/python3.8

import dis
import importlib.util
import sys

if __name__ == "__main__":
    if sys.version_info < (3, 8):
        print("This script requires Python 3.8.x")
        sys.exit(1)

    spec = importlib.util.spec_from_file_location("hidden_module", "hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    hidden_names = []
    for name in dir(module):
        if not name.startswith("__"):
            hidden_names.append(name)

    hidden_names.sort()

    for name in hidden_names:
        print(name)
