n = int(input())
for i in range (n):
    s = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if j == n - i - 1:
            s[i][j] = 1
        elif j > n - i - 1:
            s[i][j] = 2

for i in range(n):
    for j in range(n):
        print(s[i][j], end = ' ')
    print()