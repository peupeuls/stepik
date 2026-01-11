n = int(input())
s = [[0] * n for _ in range(n)]

ch = 1
for i in range(n):
    for j in range(n):
        for k in range(1, n):
            if i - j == k:
                s[i][j] = k
            if j - i == k:
                s[i][j] = k


for i in range(n):
    for j in range(n):
        print(s[i][j], end = ' ')
    print()
        
