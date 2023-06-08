#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    all_args = sum(int(arg) for arg in argv)
    print(all_args)
