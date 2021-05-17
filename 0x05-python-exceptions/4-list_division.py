#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divisions = []
    for i in range(0, list_length):
        try:
            divisions.append(my_list_1[i] / my_list_2[i])
            continue
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        divisions.append(0)
    return divisions
