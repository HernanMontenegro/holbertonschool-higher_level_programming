#!/usr/bin/python3
def uniq_add(my_list=[]):
    no_repeat_list = []
    sum_list = 0
    repeat = False

    # Normal recorrido
    for i in range(0, len(my_list)):
        # Recorrido previous index for check if they are equal
        for j in range(0, i):
            if (my_list[i] == my_list[j]):
                repeat = True
        if (not repeat):
            no_repeat_list.append(my_list[i])

        repeat = False

    for i in range(0, len(no_repeat_list)):
        sum_list += no_repeat_list[i]

    return sum_list
