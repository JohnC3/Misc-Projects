import unittest
import time


def partition(alist, start, end):

    low_index = start
    high_index = end
    piviot_index = (start + end) // 2
    pivot = alist[piviot_index]
    print('sorting ', alist[start:end + 1], 'about', pivot)
    while low_index < high_index:
        while alist[low_index] < pivot:
            low_index += 1
        while alist[high_index] > pivot:
            high_index -= 1
        print('swap', alist[low_index], alist[high_index])
        alist[low_index], alist[high_index] = alist[high_index], alist[low_index]


    print('and ya get ', alist[start:end + 1], 'about', pivot, 'return', low_index)
    return low_index


def do_quick_sort(alist, start, end):

    if start < end:

        partition_index = partition(alist, start, end)

        do_quick_sort(alist, start, partition_index - 1)
        do_quick_sort(alist, partition_index + 1, end)


def quick_sort(alist):

    start = 0
    end = len(alist) - 1
    do_quick_sort(alist, start, end)
    return alist


class TestQuickSort(unittest.TestCase):

    def test_1(self):
        l1 = [-60, 93, 51, 81, -50, 11, -29, 4, -87, -78, 85, 52, -26, 20, -94, -40, 63, 48, -39, -32]
        print(l1)
        sl1 = quick_sort(l1)
        print('sl1', sl1)
        self.assertEquals(sl1, sorted(l1))

    def test_long_list(self):
        long_list = [
            -316, -161, 181, 198, 484, -253, -104, -445, 23, -324, -276, 182,
            -204, 96, -494, -118, 330, -314, -83, 462, -117, -216, -307, 220, 385,
            303, 475, 156, -8, 309, -356, 348, 406, 265, -190, 164, 354, 110, -37,
            -94, 341, 39, 306, 212, 346, 200, -145, -481, 443, 497]

        t_start = time.time()
        quick_sorted = quick_sort(long_list)
        t_taken = time.time() - t_start
        self.assertLess(t_taken, 1000)
        self.assertListEqual(quick_sorted, sorted(long_list))

    def test_long_sorted_list(self):
        long_list = [i for i in range(0, 10000)]

        t_start = time.time()
        quick_sorted = quick_sort(long_list)
        t_taken = time.time() - t_start

        self.assertListEqual(quick_sorted, sorted(long_list))

    def test_2(self):
        l2 = [-1, 0, 1, 2, 111, 55, -111]
        sl2 = quick_sort(l2)
        print('sl2', sl2)
        self.assertEquals(sl2, sorted(l2))


if __name__ == "__main__":

    unittest.main()
