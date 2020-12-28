"""
Task from ByteDance phone screen.

Given linked list and k. Reverse it by chunks of k elements.
k >= 1
Ex1:
    Input: [1, 2, 3, 4, 5, 6, 7], k=3
    Output: [7, 4, 5, 6, 1, 2, 3]
Ex2:
    Input: [1, 2, 3], k=4
    Output: [1, 2, 3]
"""
import itertools as it
from src.linked_lists.common import ListNode


def _sequence_into_chunks(sequence, k):
    begin, end = 0, k
    while True:
        chunk = sequence[begin:end]
        if not chunk:
            break
        yield chunk
        begin += k
        end += k


def do__using_list_chunks(head, k):
    """Simple solution with O(N) additional memory + O(N) time."""
    array = list(ListNode.to_iterable(head))
    reversed_chunks = reversed(list(_sequence_into_chunks(array, k)))
    reversed_array = list(it.chain.from_iterable(reversed_chunks))
    return ListNode.from_sequence(reversed_array)


def do__using_pointers(head: ListNode, k):
    """
    The idea is the same as in simple reverse linked list (https://leetcode.com/problems/reverse-linked-list/)

    The difference is that we need one more pointer, which will point to tail of current chunk.
    When we find a tail, just do the same reverse pattern.
    """
    new_head = None
    while head is not None:
        tail = head
        # finding a tail of current chunk
        for _ in range(k - 1):
            if tail.next_node is not None:
                tail = tail.next_node
            else:
                break
        # simple reverse pattern
        tmp = tail.next_node
        tail.next_node = new_head
        new_head = head
        head = tmp
    return new_head


SOLUTIONS = [do__using_list_chunks, do__using_pointers]
