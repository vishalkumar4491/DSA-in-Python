#  merge sort

def mergeSort(a):
    l = len(a)
    if l == 0 or l == 1:
        return
    mid = l // 2
    a1 = a[: mid]
    a2 = a[mid:]

    mergeSort(a1)
    mergeSort(a2)

    merge(a1, a2, a)


def merge(a1, a2, a):
    l1 = len(a1)
    l2 = len(a2)
    i = j = k = 0
    while(i < l1 and j < l2):
        if a1[i] < a2[j]:
            a[k] = a1[i]
            i += 1
            k += 1
        else:
            a[k] = a2[j]
            j += 1
            k += 1
    while(i < l1):
        a[k] = a1[i]
        i += 1
        k += 1
    while(j < l2):
        a[k] = a2[j]
        j += 1
        k += 1


a = [int(x) for x in input().split()]
mergeSort(a)
print(a)
