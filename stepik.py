chisla1 = input().split()
n = int(chisla1[0])
m = int(chisla1[1])

matrix1 = []
for i in range(n):
    matrix1.append(input().split())
    
probel = input()

chisla2 = input().split()
k = int(chisla2[0])
p = int(chisla2[1])

matrix2 = []
for i in range(k):
    matrix2.append(input().split())

umn = [[0] * p for _ in range(n)]

for i in range(n):
    for j in range(p):
        for l in range(m):
            umn[i][j]+= int(matrix1[i][l]) * int(matrix2[l][j])

for i in range(n):
    for j in range(p):
        print(umn[i][j], end = ' ')
    print()