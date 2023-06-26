#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for i in range(x):
            try:
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end="")
                    counter += 1
            except IndexError:
                raise
    except IndexError as e:
        print()
        raise e
    finally:
        print()
        return counter
