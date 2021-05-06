#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique = []

    if len(set_1) > len(set_2):
        for i in set_1:
            if (i not in set_2):
                unique.append(i)
        for j in set_2:
            if (j not in unique and j not in set_1):
                unique.append(j)
    else:
        for i in set_2:
            if (i not in set_1):
                unique.append(i)
        for j in set_1:
            if (j not in unique and j not in set_2):
                unique.append(j)

    return dict.fromkeys(unique)
