import random
from copy import deepcopy


def run_quick_sort(alist):
    left = 0
    right = len(alist) - 1
    quick_sort(alist, left, right)
    return alist


def quick_sort(alist, left, right):

    print('quick_sort called with ', left, right)

    if left < right:

        partition_index = partition(alist, left, right)
        print('found partition_index of ', partition_index, alist)

        quick_sort(alist, left, partition_index - 1)
        quick_sort(alist, partition_index + 1, right)


def partition(alist, left, right):

    pivot_index = left
    pivot_value = alist[pivot_index]
    print('pivot_value', pivot_value)
    left_i = deepcopy(left) + 1
    right_i = deepcopy(right)
    # print('running partition with ', left_i, right_i)
    while True:

        while left_i <= right_i and alist[left_i] <= pivot_value:
            left_i += 1
            # print('left_i', left_i, right_i)

        while alist[right_i] >= pivot_value and left_i <= right_i:
            right_i -= 1

        if right_i < left_i:
            print('breaking')
            break

        print('switching', alist[right_i], alist[left_i])
        tmp = alist[left_i]
        alist[left_i] = alist[right_i]
        alist[right_i] = tmp

    # print('right_i is now split point', right_i)

    tmp = alist[right_i]
    print('swaping pivot ', alist[left], alist[right_i])
    alist[right_i] = alist[left]
    alist[left] = tmp
    return right_i



alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print('input >> ', alist)
alist = run_quick_sort(alist)
print('output >>', alist)
#
# def quickSort(alist):
#     quickSortHelper(alist, 0, len(alist)-1)
#
#
# def quickSortHelper(alist, first, last):
#     if first < last:
#
#         splitpoint = partition2(alist, first, last)
#
#         quickSortHelper(alist, first, splitpoint-1)
#         quickSortHelper(alist, splitpoint+1, last)
#
#
# def partition2(alist, first, last):
#     pivotvalue = alist[first]
#
#     leftmark = first+1
#     rightmark = last
#
#     done = False
#     while not done:
#
#         while rightmark >= leftmark and alist[leftmark] <= pivotvalue:
#             leftmark = leftmark + 1
#
#         while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
#             rightmark = rightmark - 1
#
#         if rightmark < leftmark:
#             done = True
#         else:
#             temp = alist[leftmark]
#             alist[leftmark] = alist[rightmark]
#             alist[rightmark] = temp
#
#     temp = alist[first]
#     alist[first] = alist[rightmark]
#     alist[rightmark] = temp
#
#
#     return rightmark
#
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# quickSort(alist)
# print(alist)
