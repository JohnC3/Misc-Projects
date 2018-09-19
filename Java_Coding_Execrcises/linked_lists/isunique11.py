from linked_list_base import SinglyLinkedList
import unittest


def remove_duplicates(linked_list):

    seen = set()

    head = linked_list
    current = head

    while current is not None:

        if current.next.data in seen:
            print('removing next', current.next.data)

            current.next = current.next.next
        else:
            seen.add(current.data)

        current = current.next
    return head


class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):

        ll1 = SinglyLinkedList(0)

        ll1.appendToTail(1)
        ll1.appendToTail(2)
        ll1.appendToTail(3)
        ll1.appendToTail(4)
        ll1.appendToTail(1)

        remove_duplicates(ll1)

        self.assertEqual(ll1.to_python_list(), [0, 1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()
