n = int(input())
s=[]
for i in range(n):
    s.append(str(input()).split())

flag = True
for i in range(n):
    for j in range(n):
        if s[i][j] != s[j][i]:
            print('NO')
            flag = False
            break
    if not flag:
        break        
if flag:
    print('YES')
        
         
      