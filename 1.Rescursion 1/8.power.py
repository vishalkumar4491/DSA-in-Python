# calculate the power of a by x

def power(a, x, b):
    if x == 0:
        return b
    b *= a
    return power(a, x - 1, b)


a, x = [int(x) for x in input().split()]
print(power(a, x, 1))
