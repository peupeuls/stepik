chisla = input().split()
n = int(chisla[0])
m = int(chisla[1])

for i in range (n):
    s = [[0] * m for _ in range(n)]
chislo = 1
for i in range(n):
    for j in range(m):
        s[i][j] = chislo
        chislo += 1

for i in range(n):
    for j in range(m):
        print(s[i][j], end = ' ')
    print()