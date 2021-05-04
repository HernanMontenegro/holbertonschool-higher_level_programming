#!/usr/bin/python3
def list_cpy(list):
    copy = []
    for i in range(0, len(list) - 1):
        copy.append(list[i])
    return copy


def new_in_list(my_list, idx, element):
    copy = []

    if ((idx < 0) or (idx > len(my_list) - 1)):
        copy = list_cpy(my_list)
        return copy

    for i in range(0, len(my_list)):
        if (idx == i):
            copy.append(element)
            i += 1
            continue
        copy.append(my_list[i])

    return copy
