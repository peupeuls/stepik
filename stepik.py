n = int(input())
s=[]
for i in range(n):
    s.append(str(input()).split())

maximum = 0
proverka = 0
for i in range(n):
    for j in range(n):
     if i >= n - j - 1:
      proverka = int(s[i][j])
      if maximum == 0 or maximum < proverka:
         maximum = proverka


print(maximum)
        