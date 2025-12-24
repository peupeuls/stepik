n = int(input())
s = []
for i in range (n):
   s.append(str(input()).split())

for i in range(n):
   s[i][i], s[n-1-i][i] = s[n-1-i][i],s[i][i]

for i in range(n):
   for j in range(n):
      print(s[i][j], end = ' ')
   print()
