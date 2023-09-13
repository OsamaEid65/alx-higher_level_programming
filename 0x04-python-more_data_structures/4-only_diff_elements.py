#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    f = set_1.difference(set_2)
    s = set_2.difference(set_1)
    all = s | f
    all_1 = list(all)
    all_1.sort()
    return all_1
