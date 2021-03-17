# replace all a's with b's

def replace(s, a, b, i):
    l = len(s)
    if l == 0:
        return s
    if i == l:
        return s
    if s[i] == a:
        s = s[0: i] + b + s[i + 1:]
    return replace(s, a, b, i + 1)


s = input()
print(replace(s, 'a', 'b', 0))
