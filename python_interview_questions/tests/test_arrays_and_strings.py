import pytest
import bisect
from python_interview_questions.src.arrays_and_strings import add_binary
from python_interview_questions.src.arrays_and_strings import one_away
from python_interview_questions.src.arrays_and_strings import set_matrix_zeroes
from python_interview_questions.src.arrays_and_strings import search_insert_position as sip


@pytest.mark.parametrize(
    ("first_str", "second_str", "expected"),
    [
        ("pale", "ple", True),
        ("pale", "pled", False),
        ("pales", "pled", False),
        ("pales", "pale", True),
        ("a", "a", True),
        ("aaaaaa", "a", False),
    ]
)
def test_one_away(first_str, second_str, expected):
    assert one_away.solution(first_str, second_str) == expected


@pytest.mark.parametrize(
    ("input_matrix", "expected"),
    [
        ([
            [10, 20, 0],
            [40, 50, 60],
            [90, 100, 120]
        ], [
            [0, 0, 0],
            [40, 50, 0],
            [90, 100, 0]
        ]),
        ([
            [10, 20, 30],
            [40, 0, 60],
            [90, 100, 120]
        ], [
            [10, 0, 30],
            [0, 0, 0],
            [90, 0, 120]
        ]),
        ([
            [10, 0],
            [40, 0],
        ], [
            [0, 0],
            [0, 0],
        ]),
    ]
)
def test_set_matrix_zeroes(input_matrix, expected):
    assert set_matrix_zeroes.solution(input_matrix) == expected


def test_search_insert_position():
    nums = [-5, -1, 0, 1, 3, 6, 10]
    targets = [-10] + nums + [100]
    for t in targets:
        assert sip.search_insert_recursive(nums, t) == bisect.bisect_left(nums, t)


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
    ]
)
def test_add_binary(a, b, expected):
    assert add_binary.add_binary(a, b) == expected
