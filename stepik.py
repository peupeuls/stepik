n = int(input())
s=[]
for i in range(n):
    s.append(str(input()).split())

maximum1 = 0
proverka1 = 0
for i in range(n):
    for j in range(i+1):
     if (i >= j) &  (i + j + 1 <= n):
      proverka1 = int(s[i][j])
      if maximum1 == 0 or maximum1 < proverka1:
         maximum1 = proverka1



maximum2 = 0
proverka2 = 0
for i in range(n):
    for j in range(n):
     if (i <= j) & (i + j + 1 >= n):
      proverka2 = int(s[i][j])
      if maximum2 == 0 or maximum2 < proverka2:
         maximum2 = proverka2

maximum = max(maximum1, maximum2)
print(maximum)

        