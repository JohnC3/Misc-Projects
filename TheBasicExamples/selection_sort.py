

def selection_sort(list_unsorted):
    if len(list_unsorted) == 0:
        return []
    minimum = list_unsorted[0]
    dex = 0
    for i, element in enumerate(list_unsorted):
        #
        if element < minimum:
            print(i, element)
            dex = i
            minimum = element
    print('deleting', dex)
    del list_unsorted[dex]
    print('list_unsorted', list_unsorted)

    return [minimum] + selection_sort(list_unsorted)



alist = [1, 5, 62, 4, 2, 3, 4, 5]

print('sorting ', alist)
print('output is ' ,selection_sort(alist))
