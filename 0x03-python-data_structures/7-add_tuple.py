#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = [0, 0]
    a = list(tuple_a)
    b = list(tuple_b)

    for i in range(0, 2):
        if (i > len(a) - 1):
            a.append(0)
        if (i > len(b) - 1):
            b.append(0)
        new_tuple[i] = a[i] + b[i]

    return tuple(new_tuple)
