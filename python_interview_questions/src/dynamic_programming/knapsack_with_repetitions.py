"""
Given a list of items with positive values and weights and a knapsack capacity.
Return maximum possible weight packed. Each item could be picked several times.
"""
from dataclasses import dataclass
import typing


@dataclass
class Item:
    value: int
    weight: int


def do__recursive_with_memo(items: typing.List[Item], capacity: int):
    memo = {}
    suitable_items = [i for i in items if i.weight <= capacity]
    return _dp_recursive(suitable_items, capacity, memo)


def _dp_recursive(items, capacity, memo):
    if capacity == 0:
        return 0
    if capacity not in memo:
        max_value = 0
        for i in items:
            if capacity < i.weight:
                continue
            value = _dp_recursive(items, capacity - i.weight, memo) + i.value
            if value > max_value:
                max_value = value
        memo[capacity] = max_value
    return memo[capacity]
