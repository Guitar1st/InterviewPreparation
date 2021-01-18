"""
Medium (though I think it's easy)
https://leetcode.com/problems/valid-sudoku/
"""
import typing
import itertools as it


def is_valid_sudoku(board: typing.List[typing.List[str]]) -> bool:
    return all([
        rows_valid(board),
        columns_valid(board),
        squares_valid(board),
    ])


def _line_is_valid(line):
    nums = [i for i in line if i != '.']
    return len(nums) == len(set(nums))


def _square_is_valid(board, upper_left_row, upper_left_col):
    nums = [
        board[upper_left_row + i][upper_left_col + j]
        for i in range(3) for j in range(3)
        if board[upper_left_row + i][upper_left_col + j] != '.'
    ]
    return len(nums) == len(set(nums))


def rows_valid(board):
    return all(_line_is_valid(i) for i in board)


def columns_valid(board):
    return all(_line_is_valid(i) for i in zip(*board))


def squares_valid(board):
    return all(
        _square_is_valid(board, i, j)
        for i, j in it.product([0, 3, 6], repeat=2)
    )