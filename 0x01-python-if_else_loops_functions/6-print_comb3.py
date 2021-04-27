#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 10):
        j += i
        if i == j:
            continue
        if j < 10:
            print("{:d}{:d}".format(i, j), end='')
            if i == 8 and j == 9:
                continue
            print(", ", end='')
print("")
