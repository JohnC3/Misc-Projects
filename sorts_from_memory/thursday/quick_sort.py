import unittest
import time


def do_quick_sort(arr, low, high):
    if high - low < 15:
        print('sorting,', arr[low:high + 1])

    if low < high:
        part_i = partition(arr, low, high)
        do_quick_sort(arr, low, part_i - 1)
        do_quick_sort(arr, part_i + 1, high)


def partition(arr, low, high):
    i = low
    pivot = arr[high]
    for j in range(low, high):

        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[high], arr[i] = arr[i], arr[high]
    return i


def quick_sort(arr):

    low = 0
    high = len(arr) - 1
    do_quick_sort(arr, low, high)
    return arr


class TestQuickSort(unittest.TestCase):

    def test_1(self):
        l1 = [-60, 93, 51, 81, -50, 11, -29, 4, -87, -78, 85, 52, -26, 20, -94,
              -40, 63, 48, -39, -32]
        sl1 = quick_sort(l1)
        self.assertEqual(sl1, sorted(l1))

    def test_long_list(self):
        long_list = [
            -316, -161, 181, 198, 484, -253, -104, -445, 23, -324, -276, 182,
            -204, 96, -494, -118, 330, -314, -83, 462, -117, -216, -307, 220,
            385, 303, 475, 156, -8, 309, -356, 348, 406, 265, -190, 164, 354,
            110, -37, -94, 341, 39, 306, 212, 346, 200, -145, -481, 443, 497]

        t_start = time.time()
        quick_sorted = quick_sort(long_list)
        t_taken = time.time() - t_start
        self.assertLess(t_taken, 1000)
        self.assertListEqual(quick_sorted, sorted(long_list))

    def test_long_sorted_list(self):
        long_list = [i for i in range(0, 10)]

        t_start = time.time()
        quick_sorted = quick_sort(long_list)
        t_taken = time.time() - t_start
        self.assertLess(t_taken, 1000)
        self.assertListEqual(quick_sorted, sorted(long_list))

    def test_2(self):
        l2 = [-1, 0, 1, 2, 111, 55, -111]
        sl2 = quick_sort(l2)
        self.assertEqual(sl2, sorted(l2))


if __name__ == "__main__":

    unittest.main()
