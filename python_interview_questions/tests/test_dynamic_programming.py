import pytest

from python_interview_questions.src.dynamic_programming import decode_ways
from python_interview_questions.src.dynamic_programming import knapsack_with_repetitions as kwr


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("1", 1),
        ("12", 2),
        ("226", 3),
        ("312", 2),
        ("0", 0),
    ]
)
def test_decode_ways(s, expected):
    for solution in decode_ways.SOLUTIONS:
        assert solution(s) == expected


@pytest.mark.parametrize(
    ("items", "capacity", "expected"),
    [
        (
            [kwr.Item(100, 1), kwr.Item(10, 1)],
            1,
            100
        ),
        (
            [kwr.Item(60, 10), kwr.Item(100, 20), kwr.Item(120, 30)],
            50,
            300
        ),
        (
            [kwr.Item(60, 1), kwr.Item(110, 2), kwr.Item(190, 3)],
            5,
            310
        )
    ]
)
def test_knapsack_with_repetitions(items, capacity, expected):
    assert kwr.do__recursive_with_memo(items, capacity) == expected
