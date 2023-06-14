#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    for the_key in sorted_keys:
        print("{}: {}".format(the_key, a_dictionary[the_key]))
