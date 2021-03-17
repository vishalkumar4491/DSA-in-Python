# replace pi with 3.14

def replacePi(s, p, i, c, j):
    l = len(s)
    if l == 0:
        return s
    if j == l - 1:
        return s
    if s[j] == p and s[j + 1] == i:
        s = s[0: j] + c + s[j + 2:]
    return replacePi(s, p, i, c, j + 1)


s = input()
print(replacePi(s, 'p', 'i', '3.14', 0))
