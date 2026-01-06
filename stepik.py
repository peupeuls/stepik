chisla = input().split()
n = int(chisla[0])
m = int(chisla[1])


s = [[0] * m for _ in range (n)] 

step = 1
flag = True
for i in range(n):
    for j in range(m):
        if i%2 == 0:
            s[i][j] = step
            step += 1
        if i%2 == 1:
            s[i][m-j-1] = step
            step += 1

for i in range(n):
    for j in range(m):
        print(s[i][j], end = ' ')
    print()