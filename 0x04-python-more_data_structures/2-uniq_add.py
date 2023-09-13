#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    i = 0
    prev = 0
    my_list.sort()
    while (i < len(my_list)):
        if my_list[i] != prev:
            sum += my_list[i]
        prev = my_list[i]
        i += 1
    return sum
