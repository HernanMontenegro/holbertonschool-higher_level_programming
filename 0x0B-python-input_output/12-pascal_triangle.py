#!/usr/bin/python3
''' Executable command '''


def pascal_triangle(n):
    ''' returns a list of lists of integers representing
    the Pascal’s triangle of n
    '''
    triangle = [[]]
    val = 1
    index = 0
    if (n <= 0):
        return triangle

    for i in range(1, n + 1):
        val = 1
        if (index != n - 1):
            triangle.append([])
        for j in range(1, i+1):
            triangle[index].append(val)
            val = val * (i - j) // j
        index += 1
    
    return triangle
