#!/usr/bin/python3
case = 0
for i in range(122, 96, -1):
    case = i
    if i % 2 != 0:
        case -= 32
    print('{}'.format(chr(case)), end='')
