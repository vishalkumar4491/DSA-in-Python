# calculate the last index of given number

def lastIndex(a, x, i):
    l = len(a)
    if l == 0:
        return False
    if i == -1:
        return False
    if a[i] == x:
        return i
    return lastIndex(a, x, i - 1)


a = [int(x) for x in input().split()]
x = int(input())
print(lastIndex(a, x, len(a) - 1))
