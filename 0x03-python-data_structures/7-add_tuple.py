#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Convert tuples to lists for easier manipulation
    list_a = list(tuple_a)
    list_b = list(tuple_b)

    # Less than 2 elements in tuple a
    if len(list_a) < 2:
        list_a += [0] * (2 - len(list_a))
    # More than 2 elements in tuple a
    else:
        list_a = list_a[:2]

    # Less than 2 elements in tuple b
    if len(list_b) < 2:
        list_b += [0] * (2 - len(list_b))
    # More than 2 elements in tuple b
    else:
        list_b = list_b[:2]

    # Add corresponding elements from both tuples
    sum_1 = list_a[0] + list_b[0]
    sum_2 = list_a[1] + list_b[1]

    # Return tuple with sums
    return tuple([sum_1, sum_2])
