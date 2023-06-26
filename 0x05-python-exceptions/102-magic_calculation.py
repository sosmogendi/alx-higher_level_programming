#!/usr/bin/python3
def magic_calculation(a, b):
    result2 = 0
    for i in range(1, 4):
        try:
            if i > a:
                raise Exception("Too far")
            result2 += (a ** b) / i
        except:
            result2 = b + a
            break
    return result2
