from python_interview_questions.src.linked_lists import common as linked_lists_common
from python_interview_questions.src.linked_lists import reverse_by_k


class TestCommon:
    def test_list_node(self):
        n2 = linked_lists_common.ListNode(2)
        n1 = linked_lists_common.ListNode(1, n2)
        assert n1.next_node == n2

    def test_linked_list_from_sequence(self):
        linked_list1 = linked_lists_common.ListNode.from_sequence((1, 2, 3))
        linked_list2 = linked_lists_common.ListNode.from_sequence((1, 2, 4))
        n3 = linked_lists_common.ListNode(3)
        n2 = linked_lists_common.ListNode(2, n3)
        n1 = linked_lists_common.ListNode(1, n2)
        print("qq")
        assert n1 == linked_list1
        assert n1 != linked_list2

    def test_linked_list_to_iterable(self):
        n2 = linked_lists_common.ListNode(2)
        n1 = linked_lists_common.ListNode(1, n2)
        assert list(n1.to_iterable()) == [1, 2]


def test_reverse_by_k():
    test1, k1 = linked_lists_common.ListNode.from_sequence([1, 2, 3, 4, 5]), 1
    expected1 = linked_lists_common.ListNode.from_sequence([5, 4, 3, 2, 1])
    test2, k2 = linked_lists_common.ListNode.from_sequence([1, 2, 3, 4, 5, 6, 7]), 3
    expected2 = linked_lists_common.ListNode.from_sequence([7, 4, 5, 6, 1, 2, 3])
    test3, k3 = linked_lists_common.ListNode.from_sequence([1, 2, 3, 4]), 7
    expected3 = linked_lists_common.ListNode.from_sequence([1, 2, 3, 4])
    for solution in reverse_by_k.SOLUTIONS:
        assert solution(test1, k1) == expected1
        assert solution(test2, k2) == expected2
        assert solution(test3, k3) == expected3
