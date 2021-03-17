# in a cirlce there are some people calculate who will survive at last

# def josephus(n, k):
#     if n == 1:
#         return 1
#     return (josephus(n - 1, k) + k) % n

#
def josephus2(n, k):
    if n == 1:
        return 1
    return (josephus2(n - 1, k) + k - 1) % n + 1


n = int(input())
k = int(input())
# print(josephus(n, k))
print(josephus2(n, k))
