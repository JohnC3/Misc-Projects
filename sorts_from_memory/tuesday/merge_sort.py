
def merge(list1, list2):
    print('merging ', list1, list2)

    merged_list = []

    i, j = 0, 0

    print('i < ', len(list1) - 1,  'j < ', len(list2) - 1)

    while i < len(list1) and j < len(list2):

        if list1[i] < list2[j]:

            merged_list.append(list1[i])
            print('adding from i', i, list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            print('adding from j', j, list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list





def merge_sort(alist):

    if len(alist) == 0:
        print('zero len')
        return []

    if len(alist) == 1:
        print('<=1 returning ', alist)
        return alist

    else:
        middle = len(alist) // 2

        print('splitting on ', middle, type(middle))

        lower = merge_sort(alist[:middle])
        upper = merge_sort(alist[middle:])

        return merge(lower, upper)




if __name__ == "__main__":
    test_value = [6, 3, 82, 1, 34, -6]
    print(merge_sort(test_value))

    print(merge([-5, 2], [1, 55]))
