#!/usr/bin/python3

def delete_at(my_list, idx):
    my_new_list = []
    for i in range(len(my_list)):
        if i >= 0 and i < len(my_list) and i != idx:
            my_new_list.append(my_list[i])
    return my_new_list
