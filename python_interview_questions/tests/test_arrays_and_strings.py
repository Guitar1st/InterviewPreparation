import pytest
from python_interview_questions.src.arrays_and_strings import one_away
from python_interview_questions.src.arrays_and_strings import set_matrix_zeroes


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
