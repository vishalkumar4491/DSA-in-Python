# calculate the all the indexes of given number

def allIndexes(a, x, i, li):
    l = len(a)
    if l == 0:
        return False
    if i == l and len(li) == 0:
        return False
    if i == l and len(li) != 0:
        return li
    if a[i] == x:
        li.append(i)
    return allIndexes(a, x, i + 1, li)


a = [int(x) for x in input().split()]
x = int(input())
print(allIndexes(a, x, 0, []))
