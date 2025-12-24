n = int(input())
s = []
for i in range (n):
   s.append(str(input()).split())

for i in range(n//2):
   for j in range(n):
      s[i][j], s[n-1-i][j] = s[n-1-i][j], s[i][j]

for i in range(n):
   for j in range(n):
      print(s[i][j], end = ' ')
   print()