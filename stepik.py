n = int(input())
s=[]
for i in range(n):
    s.append(str(input()).split())

flag = True
for i in range(n):
    for j in range(n):
        if s[i][j] != s[n - j - 1][n - i - 1]:
            print('NO')
            flag = False
            break
    if not flag:
        break
if flag:
    print('YES')
