import random
import unittest
import sys

print('Recursion limit is!', sys.getrecursionlimit())
# sys.setrecursionlimit(50)    /

def merge(listA, listB):
    indexA, indexB = 0, 0
    merged_list = []
    while indexA < len(listA) and indexB < len(listB):

        if listA[indexA] <= listB[indexB]:
            merged_list.append(listA[indexA])
            indexA += 1
        else:
            merged_list.append(listB[indexB])
            indexB += 1

    while indexA < len(listA):
        merged_list.append(listA[indexA])
        indexA += 1
    while indexB < len(listB):
        merged_list.append(listB[indexB])
        indexB += 1
    return merged_list

def merge_sort(alist, recursion_depth=0):
    print('recursion_depth', recursion_depth)
    if len(alist) < 2:
        return alist
    middle = len(alist) // 2
    print('middle', middle, 'left', alist[:middle])
    print('middle', middle, 'right', alist[middle:])
    left = merge_sort(alist[:middle], recursion_depth + 1)
    right = merge_sort(alist[middle:], recursion_depth + 1)

    return merge(left, right)


class TestMergeSort(unittest.TestCase):

    def test_merge_sort_1(self):

        l1 = [-60, 93, 51, 81, -50, 11, -29, 4, -87, -78, 85, 52, -26, 20, -94, -40, 63, 48, -39, -32]
        print(l1)
        sl1 = merge_sort(l1)
        print(sl1)
        self.assertListEqual(sl1, sorted(l1))

    def test_merge_sort_2(self):

        l2 = [6, 3, 82, 1, 34, -6]
        sl2 = merge_sort(l2)
        print(sl2)
        self.assertListEqual(sl2, sorted(l2))

if __name__ == "__main__":
    unittest.main()
