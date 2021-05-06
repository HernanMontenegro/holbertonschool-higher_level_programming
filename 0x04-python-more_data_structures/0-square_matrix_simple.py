#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in range(0, len(matrix)):
        # Creation of a new list inside our list
        new_matrix.append([])
        for j in range(0, len(matrix[i])):
            # Creation of a new element
            new_matrix[i].append(j)
            # Assignment of this new element
            new_matrix[i][j] = matrix[i][j] ** 2

    return new_matrix
