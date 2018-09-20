import unittest


def merge(left, right):

    print('merging', left, 'with', right)

    Li, Ri = 0, 0
    output = []
    while Li < len(left) and Ri < len(right):

        if left[Li] < right[Ri]:
            output.append(left[Li])
            Li += 1
        else:
            output.append(right[Ri])
            Ri += 1

    while Li < len(left):
        output.append(left[Li])
        Li += 1

    while Ri < len(right):
        output.append(right[Ri])
        Ri += 1

    print('gave', output)
    return output


# def space_saving_merge(left, right):
#
#     print('merging', left, 'with', right)
#     Li, Ri = 0, len(left)
#
#     while Li < len(left) and Ri > 0:
#
#         while left[Li] < right[Ri]:
#             Li += 1
#
#         while right[Ri]


def merge_sort(arr):

    print('merge_sort on, ',arr)

    if arr is not None and len(arr) > 1:
        middle = len(arr) // 2

        left = merge_sort(arr[0: middle])
        right = merge_sort(arr[middle:])

        return merge(left, right)

    else:
        return arr






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
