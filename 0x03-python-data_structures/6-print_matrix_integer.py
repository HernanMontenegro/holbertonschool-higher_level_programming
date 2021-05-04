#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end='')
            if (j != len(matrix[i]) - 1):
                print(" ", end='')
        print("")
