# print number from 1 to n

def printN(n):
    if n == 0:
        return
    printN(n - 1)
    print(n, end=' ')
    return


def printN2(n, k=1):
    if n == 0:
        return
    print(k, end=' ')
    return printN2(n - 1, k + 1)


def printNto1(n):
    if n == 1:
        return 1
    print(n, end=' ')
    return printNto1(n - 1)


n = int(input())
print(printN(n))
print(printN2(n))
print(printNto1(n))
