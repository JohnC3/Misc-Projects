

def bubble_sort(un_sorted):
    list_unsorted = True
    while list_unsorted:
        list_unsorted = False
        for p1 in range(0, len(un_sorted) - 1):
            p2 = p1 + 1

            if un_sorted[p1] > un_sorted[p2]:
                list_unsorted = True
                tmp = un_sorted[p1]
                un_sorted[p1] = un_sorted[p2]
                un_sorted[p2] = tmp

    return un_sorted

alist = [1, 5, 62, 4, 2, 3, 4, 5]

print('sorting ', alist)
print('output is ' ,bubble_sort(alist))
