#!/usr/bin/python3
"""rotate 2d matrix"""


def rotate_2d_matrix(matrix):
    """edit 2d matirx in place rotate 90 deg clockwise"""
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)    