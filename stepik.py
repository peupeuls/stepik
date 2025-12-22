n = int(input())
m = int(input())
s=[]
for i in range(n):
    s.append(str(input()).split())

maximum = 0
proverka = 0
mnogo = []
for i in range(n):
    for j in range(m):
      proverka = int(s[i][j])
      if maximum == 0 or maximum < proverka:
         maximum = proverka
    mnogo.append(maximum)
bolshoi = max(mnogo)

flag = False
for i in range(n):
   for j in range(m):
      if s[i][j] == str(bolshoi):
         print(str(i) + ' ' + str(j))
         flag = True
         break
   if flag:
      break
         

