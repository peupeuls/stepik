n = int(input())
m = int(input())

mult = [[0] * m for _ in range(n)]
for i in range(n):
   for j in range(m):
      mult[i][j] = i * j
      print(mult[i][j], end = ' ')
   print()