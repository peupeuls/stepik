chisla = input().split()
n = int(chisla[0])
m = int(chisla[1])

matrix1 = []
matrix2 = []
for i in range(n):
    matrix1.append(input().split())
probel = input()
for i in range(n):
    matrix2.append(input().split())

summa = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        summa[i][j] = int(matrix1[i][j]) + int(matrix2[i][j])

for i in range(n):
    for j in range(m):
        print(summa[i][j], end = ' ')
    print()