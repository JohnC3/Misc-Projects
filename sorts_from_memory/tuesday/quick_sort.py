import unittest

def partition(alist, left, right):
    print('partitioning from ', alist[left: right + 1])
    middle = (left + right) // 2

    print('middle is ', middle)

    val = alist[middle]

    while left < right:

        while alist[left] < val:
            left += 1

        while alist[right] > val:
            right -= 1

        if alist[left] > alist[right]:
            temp = alist[left]
            alist[left] = alist[right]
            alist[right] = temp
            print('swapping ', alist[left], alist[right])
        else:
            print('do nothing I guess?')

    return middle


def quick_sort_process(alist, left, right):


    partition_index = partition(alist, left, right)

    if partition_index > left:
        quick_sort_process(alist, left, partition_index - 1)
    if partition_index < right:
        quick_sort_process(alist, partition_index + 1, right)

def quick_sort(alist):
    left = 0
    right = len(alist) - 1

    quick_sort_process(alist, left, right)
    return alist


class TestQuickSort(unittest.TestCase):

    def test_1(self):
        l1 = [-1, 10, 3, 14]
        self.assertListEqual(quick_sort(l1), sorted(l1))

    def test_2(self):
        l1 = [-1, 0, 1, 2, 55, 111]
        self.assertListEqual(quick_sort(l1), sorted(l1))


if __name__ == "__main__":

    unittest.main()
