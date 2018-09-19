from linked_list_base import SinglyLinkedList

def get_k_to_last(linkedList, k):

    k_ahead, slow = linkedList, linkedList

    for _i in range(k):
        if k_ahead.next is None:
            return None
        k_ahead = k_ahead.next

    while k_ahead.next is not None:
        k_ahead = k_ahead.next
        slow = slow.next

    return slow


ll = SinglyLinkedList(0)
ll.append_python_list([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(get_k_to_last(ll, 1))
