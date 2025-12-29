chisla = input().split()
n = int(chisla[0])
m = int(chisla[1])

for i in range (n):
    s = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i + j)%2 == 0:
            s[i][j] = "."
        else:
            s[i][j] = "*"
for i in range(n):
    for j in range(m):
        print(s[i][j], end = ' ')
    print()
