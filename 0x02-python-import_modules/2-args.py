#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    args_count = len(argv)

    if args_count == 0:
        print("0 arguments.")
    else:
        atleast_one = "s" if args_count > 1 else ""
        print("{} argument{}:".format(args_count, atleast_one))
        for j, arg in enumerate(argv):
            print("{}: {}".format(j + 1, arg))
