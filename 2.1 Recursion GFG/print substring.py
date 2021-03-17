# print all substring of given string

def printSubstring(s, cur, i):
    if i == len(s):
        print(cur, end=' ')
        return

    printSubstring(s, cur, i + 1)
    printSubstring(s, cur + s[i], i + 1)


s = input()
printSubstring(s, '', 0)
