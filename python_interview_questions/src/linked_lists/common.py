from dataclasses import dataclass
import typing


@dataclass
class ListNode:
    value: typing.Any = None
    next_node: typing.Optional[typing.Any] = None

    @classmethod
    def from_sequence(cls, input_list: typing.Sequence):
        head = None
        for i in reversed(input_list):
            head = cls(i, head)
        return head

    def to_iterable(self):
        current_node = self
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next_node
