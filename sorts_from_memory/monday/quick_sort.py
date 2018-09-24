import unittest
import time


def partition(alist, low, high):


    middle = (low + high) // 2
    pivot = alist[middle]
    print('partition', alist[low:high + 1], 'about pivot', pivot)
    low_itter = 0
    high_itter = high

    while low_itter < high_itter:

        while alist[low_itter] < pivot:
            low_itter += 1

        while alist[high_itter] > pivot:
            high_itter -= 1

        print('swap', alist[low_itter], alist[high_itter])

        temp = alist[low_itter]
        alist[low_itter] = alist[high_itter]
        alist[high_itter] = temp

    print('results in', alist[low:high + 1], ' returning ', low_itter)
    return low_itter




def _quick_sort(alist, low, high):

    if low < high:

        Pi = partition(alist, low, high)

        _quick_sort(alist, low, Pi - 1)
        _quick_sort(alist, Pi + 1, high)


def quick_sort(list_input):

    _quick_sort(list_input, 0, len(list_input) - 1)
    return list_input



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
