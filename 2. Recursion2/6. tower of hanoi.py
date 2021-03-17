def TOH(n, a, b, c):
    if n == 1:
        print('move 1st disk from ', a, "to ", c)
        return
    TOH(n - 1, a, c, b)
    print('move ', n, 'th disk from ', a, ' to', c)
    TOH(n - 1, b, a, c)


n = int(input())
TOH(n, 'a', 'b', 'c')
