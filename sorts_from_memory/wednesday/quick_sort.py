import unittest
import sys

sys.setrecursionlimit(3000)


def partition(arr, left, right):

    lowest_seen = left - 1
    high_i = left
    pivot = arr[right]
    print('arr', arr)
    print('left', left, 'right', right)
    for high_i in range(left, right):

        if arr[high_i] <= pivot:

            lowest_seen += 1
            arr[lowest_seen], arr[high_i] = arr[high_i], arr[lowest_seen]


    print('swapping pivot point from ', left, lowest_seen)
    print('swap', arr[left], arr[lowest_seen])

    arr[right], arr[lowest_seen + 1] = arr[lowest_seen + 1], arr[right]

    print('partition complete arr', arr)
    return lowest_seen + 1


def do_quick_sort(alist, left, right):

    if left < right:

        part_index = partition(alist, left, right)

        if part_index > left:
            do_quick_sort(alist, left, part_index - 1)
        if part_index < right:
            do_quick_sort(alist, part_index + 1, right)
    return alist

def quick_sort(alist):

    return do_quick_sort(alist, 0, len(alist) - 1)

class TestQuickSort(unittest.TestCase):

    def test_1(self):
        l1 = [-60, 93, 51, 81, -50, 11, -29, 4, -87, -78, 85, 52, -26, 20, -94, -40, 63, 48, -39, -32]
        print(l1)
        sl1 = quick_sort(l1)
        print('sl1', sl1)
        self.assertEquals(sl1, sorted(l1))

    def test_2(self):
        l2 = [-1, 0, 1, 2, 111, 55, -111]
        sl2 = quick_sort(l2)
        print('sl2', sl2)
        self.assertEquals(sl2, sorted(l2))


if __name__ == "__main__":

    unittest.main()
