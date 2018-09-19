import unittest


class Node:

    def __init__(self, data):

        self.data = data
        self.next = None

    def appendToTail(self, d):
        end = Node(d)
        n = self

        while n.next is not None:
            n = n.next
        n.next = end

    def __str__(self):
        return '{}'.format(self.data)


class SinglyLinkedList(Node):

    # def __init__(self, data):
    #
    #     self.head = super().__init__(data)

    def delete_node(self, value):

        if self.head.data == value:
            self.head = self.head.next
            return 0
        cur = self.head
        while cur.next is not None:

            if cur.next.data == value:
                cur.next = cur.next.next
                return 0
            cur = cur.next

    def to_python_list(self):
        py_list = []
        cur = self

        while cur.next is not None:
            py_list.append(cur.data)
            cur = cur.next
        py_list.append(cur.data)
        return py_list

    def append_python_list(self, list_to_add):
        """
        Takes a normal python list appends it to the end of this
        """
        cur = self

        for element in list_to_add:
            eNode = Node(element)
            cur.next = eNode
            cur = eNode


class TestNodeClass(unittest.TestCase):

    def test_append(self):

        base = Node(1)

        base.appendToTail(2)

        self.assertEqual(base.next.data, 2)

    def test_to_python_list(self):

        empty_list = SinglyLinkedList(None)

        self.assertEqual(empty_list.to_python_list(), [None])


if __name__ == "__main__":

    unittest.main()
