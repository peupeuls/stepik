n = int(input())
s = [ ['.'] * n for _ in range(n)]

seredina = (n-1)/2
for i in range(n):
    for j in range(n):
        if i == j:
            s[i][j] = '*'
        elif i == n - j - 1:
            s[i][j] = '*'
        elif i == seredina:
            s[i][j] = '*'
        elif j == seredina:
            s[i][j] = '*'

for i in range(n):
    for j in range(n):
        print(s[i][j], end = ' ')
    print()