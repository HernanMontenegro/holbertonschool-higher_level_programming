#!/usr/bin/python3
"""Executable command

    You can test this function in
    /test/2-matrix_divided.txt
"""


def matrix_divided(matrix, div):
    """divide a matrix by a number
        usage: add_integer(list of list, int), add_integer(list of list, float)
    """

    # ============== Some edge cases ====================
    # div is not an int or a float partner
    if (type(div) != int and type(div) != float):
        raise TypeError("div must be a number")
    # Try a division by 0... sale mal
    elif (div == 0):
        raise ZeroDivisionError("division by zero")
    # Matrix is NOT a matrix O.-
    elif (matrix is None or
            type(matrix) != list or
            not (all(isinstance(i, list) for i in matrix))):
                raise TypeError("matrix must be a matrix" +
                                " (list of lists) of integers/floats")

    # Copy every nested list
    divided = [i.copy() for i in matrix]
    row_len = 0

    # Start dividing one by one, taking into account of edge cases
    for i in range(0, len(divided)):
        for j in range(0, len(divided[i])):
            # Checks when a list is different length (ノ ͡⚈ ͜ʖ ͡⚈)ノ
            if (len(divided[0]) != len(divided[i])):
                raise TypeError("Each row of the matrix" +
                                " must have the same size")

            # May we have an impostor type in the list ( ͡⚈ ͜ʖ ͡⚈)
            if (type(divided[i][j]) == int or type(divided[i][j]) == float or
                    type(divided[i][j]) == bool):
                divided[i][j] /= div
                divided[i][j] = round(divided[i][j], 2)
            else:
                raise TypeError("matrix must be a matrix" +
                                " (list of lists) of integers/floats")
    return divided
