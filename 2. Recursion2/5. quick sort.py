# quick sort

def quickSort(a, si, ei):
    if si >= ei:
        return
    pivotIndex = partition(a, si, ei)
    quickSort(a, si, pivotIndex - 1)
    quickSort(a, pivotIndex + 1, ei)


def partition(a, si, ei):
    pivot = a[si]
    # find the number of elements less than pivot
    count = 0
    for i in range(si, ei + 1):
        if a[i] < pivot:
            count += 1
    a[si + count], a[si] = a[si], a[si + count]
    pivotIndex = si + count
    i = si
    j = ei
    while(i < j):
        if a[i] < pivot:
            i += 1
        elif a[j] >= pivot:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    return pivotIndex


a = [int(x) for x in input().split()]

# print(partition(a, 0, len(a) - 1))
quickSort(a, 0, len(a) - 1)
print(a)
