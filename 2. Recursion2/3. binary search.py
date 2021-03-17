# binary search

def bs(a, x, i, j):
    if i > j:
        return -1
    mid = (i + j) // 2
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return bs(a, x, i, mid - 1)
    else:
        return bs(a, x, mid + 1, j)


a = [int(x) for x in input().split()]
x = int(input())
print(bs(a, x, 0, len(a) - 1))
