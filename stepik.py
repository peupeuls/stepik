n = int(input())
m = int(input())
s=[]
for i in range(n*m):
    s.append(input())

matrix = []
matrix.append([s[0]])
for i in range(1, n*m):
        if i % m != 0:
            matrix[-1].append(s[i])
        else:
             matrix.append([s[i]])

for i in range(n):
     for j in range(m):
          print(matrix[i][j], end=' ')
        
     print()

print()
for j in range(m):
     for i in range(n):
          print(matrix[i][j], end=' ')
     print()
