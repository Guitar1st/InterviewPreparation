import pytest

from python_interview_questions.src.dynamic_programming import decode_ways


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("1", 1),
        ("12", 2),
        ("226", 3),
        ("0", 0),
    ]
)
def test_decode_ways(s, expected):
    for solution in decode_ways.SOLUTIONS:
        assert solution(s) == expected
