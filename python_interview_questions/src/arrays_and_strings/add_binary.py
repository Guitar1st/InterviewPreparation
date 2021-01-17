"""
Easy
https://leetcode.com/problems/add-binary/
"""
import itertools


def add_binary(a: str, b: str) -> str:
    """
    This is not the fastest solution, but here I did not use int to str and str to int casts.
    """
    if a == '0':
        return b
    if b == '0':
        return a
    return _add(a, b)


def _add(a, b):
    result = []
    carry = '0'
    for i, j in itertools.zip_longest(reversed(a), reversed(b), fillvalue='0'):
        # it is possible to use pattern matching here (match i, j, carry)
        # if used, we could not rely on integers at all
        # python does not support fancy matching syntax, so I decided not to implement solution that way
        curr_val = sum(1 for k in [i, j, carry] if k == '1')
        carry = '0' if curr_val < 2 else '1'
        a = '1' if curr_val % 2 == 1 else '0'
        result.append(a)
    if carry == '1':
        result.append(carry)
    return ''.join(reversed(result))
