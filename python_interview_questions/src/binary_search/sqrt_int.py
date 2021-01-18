"""
Easy
https://leetcode.com/problems/sqrtx/
"""


def my_sqrt_binsearch(x: int) -> int:
    """
    Simple binsearch solution.

    The main key to the solution - understand where the binary search ends.
    It is the first int, which square is greater than x.
    """
    if x == 0:
        return 0
    if x <= 3:
        return 1
    lo = 2
    hi = x // 2 + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if mid ** 2 > x:
            hi = mid
        else:
            lo = mid + 1
    return lo - 1
