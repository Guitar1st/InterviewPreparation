"""
Task from Facebook phone screen (2018).

https://leetcode.com/problems/decode-ways
"""

TWO_WAYS = frozenset(map(str, range(10, 27)))


def do__recursive_with_memo(s: str) -> int:
    memo = {}
    return _decode_ways(s, 0, memo)


def _decode_ways(s, i, memo):
    if i >= len(s):
        return 1
    if s[i] == "0":
        return 0
    if i not in memo:
        if s[i:i + 2] in TWO_WAYS:
            memo[i] = _decode_ways(s, i + 1, memo) + _decode_ways(s, i + 2, memo)
        else:
            memo[i] = _decode_ways(s, i + 1, memo)
    return memo[i]


SOLUTIONS = [do__recursive_with_memo]
