n = int(input())
s=[]
for i in range(n):
    s.append(str(input()).split())

summa = 0
bolshe = 0
for i in range(n):
    summa = 0
    srednee = 0
    bolshe = 0
    for j in range(n):
     summa += int(s[i][j])
     srednee = summa/n
    for j in range(n):
       if int(s[i][j]) > srednee:
          bolshe += 1
       else: continue 
    print(bolshe)
