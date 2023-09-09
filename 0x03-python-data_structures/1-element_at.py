#!/usr/bin/pytho3
def element_at(my_list, idx):
    if idx < 0:
        return 'None'
    elif idx > len(my_list)-1:
        return 'None'
    for i in range (0,len(my_list)):
        if my_list[idx]==my_list[i]:
            return my_list[i]
