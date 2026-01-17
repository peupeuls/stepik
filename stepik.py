m = int(input())
n = int(input())

dom = [input() for _ in range(m)]
spis = [input() for _ in range(n)]
for i in range(n):
    if spis[i] in dom:
        print('YES')
    else:
        print('NO')