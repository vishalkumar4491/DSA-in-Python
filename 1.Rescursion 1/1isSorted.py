# given list of size n is sorted or not

def isSorted(a, n):
    if n == 0 or n == 1:
        return True
    if a[0] > a[1]:
        return False
    # it uses to many memory
    b = a[1:]
    return isSorted(b, n - 1)


def isSorted2(a, n, i):
    if i == n - 1 or i == n:
        return True
    if a[i] > a[i + 1]:
        return False
    return isSorted2(a, n, i + 1)


a = [1, 3, 4, 6]
print(isSorted(a, 4))
print(isSorted2(a, 4, 0))
