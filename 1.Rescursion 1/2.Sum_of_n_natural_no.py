# find the sum of first n natural number

def sofnn(n):
    if n == 0:
        return 0
    return n + sofnn(n - 1)


def sofnn2(n, k):
    if n == 0:
        return k
    return sofnn2(n - 1, k + n)


t = int(input())
print(sofnn(t))
print(sofnn2(t, 0))
