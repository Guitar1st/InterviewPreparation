"""
Easy
https://leetcode.com/problems/search-insert-position/

This is classic binary search. In python it is bisect.bisect_left
"""
import typing


def search_insert_recursive(nums: typing.List[int], target: int) -> int:
    """
    Not so optimal because of recursion, but quite straightforward solution.
    Iterative solution could be found at bisect.bisect_left
    """
    if not nums:
        return 0
    return _binsearch(nums, 0, len(nums), target)


def _binsearch(nums, lo, hi, t):
    if lo >= hi:
        return lo
    mid = (lo + hi) // 2
    if t == nums[mid]:  # this branch will save one recursive call assuming there is no repetitions
        return mid
    elif t < nums[mid]:
        return _binsearch(nums, lo, mid, t)
    else:
        return _binsearch(nums, mid + 1, hi, t)
