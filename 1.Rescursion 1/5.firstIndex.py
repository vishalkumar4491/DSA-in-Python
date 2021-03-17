# calculate the first index of given number

def firstIndexOfNumber(a, x, i):
    l = len(a)
    if l == 0:
        return False
    if i == l:
        return False
    if a[i] == x:
        return i
    return firstIndexOfNumber(a, x, i + 1)


a = [int(x) for x in input().split()]
x = int(input())
print(firstIndexOfNumber(a, x, 0))
