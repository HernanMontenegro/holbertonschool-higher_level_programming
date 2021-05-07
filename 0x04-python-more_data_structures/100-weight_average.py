#!/usr/bin/python3
def weight_average(my_list=[]):
    res = 0
    temp = 0
    divi = 0

    if (0 == len(my_list)):
        return 0

    for item in my_list:
        for j in range(0, len(item)):
            if (j == 0):
                temp = item[j]
                continue
            temp *= item[j]
            divi += item[j]
        res += temp

    return res / divi
