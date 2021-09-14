#!/usr/bin/python3
''' finds a peak in a list of unsorted integers '''


def find_peak(int_list):
    ''' func '''

    if len(int_list) == 0:
        return None
    elif len(int_list) == 1:
        return int_list[0]
    elif len(int_list) == 2:
        return max(int_list)

    the_half = int(len(int_list) / 2)
    mid = int_list[the_half]

    if mid > int_list[the_half - 1] and mid > int_list[the_half + 1]:
        return mid
    elif mid < int_list[the_half - 1]:
        return find_peak(int_list[:the_half])
    else:
        return find_peak(int_list[the_half + 1:])
