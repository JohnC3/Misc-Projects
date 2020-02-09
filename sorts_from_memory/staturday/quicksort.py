import random


def shuffle_around(array, left, right):
    print("INPUT", array, array[left: right])
    pivot_idx = left

    pivot = array[pivot_idx]
    print("INPUT", array, array[left: right], "pivot value", pivot)

    # array[pivot_idx], array[left] = array[left], array[pivot_idx]

    lesser_idx = left + 1
    for i in range(left + 1, right):
        if array[i] < pivot:
            array[i], array[lesser_idx] = array[lesser_idx], array[i]

            lesser_idx += 1
    # Now swap lesser_idx with piv lesser_idx is 1 more then the idex of the number less then pivot
    array[lesser_idx - 1], array[pivot_idx] = array[pivot_idx], array[lesser_idx - 1]
    print(array)
    return lesser_idx - 1


def quick_sort(array, left, right):
    if left < right:

        partition_location = shuffle_around(array, left, right)
        quick_sort(array, left, partition_location)
        quick_sort(array, partition_location + 1, right)


if __name__ == "__main__":
    pass
    tc = [5, 3, 1, 77, 51, 2]
    quick_sort(tc, 0, len(tc))

    print(tc)
    print(tc == sorted(tc))