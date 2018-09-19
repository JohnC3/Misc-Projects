def merge_sort(alist):

    if len(alist) > 1:
        low = 0
        high = len(alist)

        middle = (high - low) // 2
        lefthalf = alist[:middle]
        righthalf = alist[middle:]

        left = 0
        right = 0
        current = 0
        merge_sort(lefthalf)
        merge_sort(righthalf)
        while left < len(lefthalf) and right < len(righthalf):

            if lefthalf[left] < righthalf[right]:
                alist[current] = lefthalf[left]
                left += 1
                current += 1

            else:
                alist[current] = righthalf[right]
                right += 1
                current += 1

        while left < len(lefthalf):
            alist[current] = lefthalf[left]
            left += 1
            current += 1

        while right < len(righthalf):
            alist[current] = righthalf[right]
            right += 1
            current += 1

        return alist
    print('merging', alist)


def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)

print(alist)

alist = [54,26,93,17,77,31,44,55,20]
merge_sort(alist)
print(alist)
