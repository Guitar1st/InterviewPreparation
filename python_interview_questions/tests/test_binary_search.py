import math
from python_interview_questions.src.binary_search import sqrt_int


def test_sqrt_int():
    for i in range(900):
        assert sqrt_int.my_sqrt_binsearch(i) == int(math.sqrt(i))
