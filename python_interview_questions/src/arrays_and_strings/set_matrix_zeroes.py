"""
https://leetcode.com/problems/set-matrix-zeroes/
"""


def solution(matrix):
    if not matrix:
        return matrix
    zero_columns, zero_rows = set(), set()
    for row_n in range(len(matrix)):
        for col_n in range(len(matrix[row_n])):
            if matrix[row_n][col_n] == 0:
                zero_columns.add(col_n)
                zero_rows.add(row_n)
    for col_n in zero_columns:
        for row_n in range(len(matrix)):
            matrix[row_n][col_n] = 0
    for row_n in zero_rows:
        for col_n in range(len(matrix[row_n])):
            matrix[row_n][col_n] = 0
    return matrix
