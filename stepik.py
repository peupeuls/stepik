n = int(input())
s=[]
for i in range(n):
    s.append(str(input()).split())


flag = True

for i in range(n):
    for j in range(1, n + 1):
        if str(j) not in s[i] or str(j) not in [s[k][i] for k in range(n)]:
            print('NO')
            flag = False
            break
    if not flag:
        break
if flag:
    print('YES')

