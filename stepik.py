n = int(input())
m = int(input())
s=[]
for i in range(n):
    s.append(str(input()).split())
columns = str(input()).split()
col1 = int(columns[0])
col2 = int(columns[1])

for i in range(n):
    s[i][col1], s[i][col2] = s[i][col2],s[i][col1]
for i in range(n):
    for j in range(m):
        print(s[i][j], end = ' ')
    print()