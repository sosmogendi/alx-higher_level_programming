#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    w_sum = 0
    total_w = 0

    for score, weight in my_list:
        w_sum += score * weight
        total_w += weight

    return w_sum / total_w
