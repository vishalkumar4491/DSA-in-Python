# calculaye the factorial of given number n

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fact(n, k=1):
    if n == 0:
        return k
    k = k * n
    return fact(n - 1, k)


n = int(input())
print(factorial(n))
print(fact(n, 1))
