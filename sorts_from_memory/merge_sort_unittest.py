import unittest
import time


def merge_sort(arr):
    pass


class TestMergeSort(unittest.TestCase):

    def test_merge_sort_1(self):

        l1 = [-60, 93, 51, 81, -50, 11, -29, 4, -87, -78, 85, 52, -26, 20, -94, -40, 63, 48, -39, -32]
        print(l1)
        sl1 = merge_sort(l1)
        print(sl1)
        self.assertListEqual(sl1, sorted(l1))

    def test_long_list(self):
        long_list = [
            -316, -161, 181, 198, 484, -253, -104, -445, 23, -324, -276, 182,
            -204, 96, -494, -118, 330, -314, -83, 462, -117, -216, -307, 220,
            385, 303, 475, 156, -8, 309, -356, 348, 406, 265, -190, 164, 354,
            110, -37, -94, 341, 39, 306, 212, 346, 200, -145, -481, 443, 497]

        t_start = time.time()
        quick_sorted = merge_sort(long_list)
        t_taken = time.time() - t_start
        self.assertLess(t_taken, 1000)
        self.assertListEqual(quick_sorted, sorted(long_list))

    def test_long_sorted_list(self):
        long_list = [i for i in range(0, 10000)]

        t_start = time.time()
        quick_sorted = merge_sort(long_list)
        t_taken = time.time() - t_start

        self.assertListEqual(quick_sorted, sorted(long_list))

    def test_merge_sort_2(self):

        l2 = [6, 3, 82, 1, 34, -6]
        sl2 = merge_sort(l2)
        print(sl2)
        self.assertListEqual(sl2, sorted(l2))

if __name__ == "__main__":
    unittest.main()
