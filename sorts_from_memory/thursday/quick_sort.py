import unittest
import time

def do_quick_sort(arr, low, high):
    print('sorting,', arr[low:high + 1])

    if low < high:
        part_i = partition(arr, low, high)
        do_quick_sort(arr, low, part_i - 1)
        do_quick_sort(arr, part_i + 1, high)


def partition(arr, low, high):

    i = low - 1
    pivot = arr[high]
    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[high], arr[i+1] = arr[i+1], arr[high]
    return i + 1


def quick_sort(arr):

    low = 0
    high = len(arr) - 1
    do_quick_sort(arr, low, high)
    return arr





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
