n = int(input())
s=[]
for i in range(n):
    s.append(str(input()).split())

levaya = 0
pravaya = 0
verhnaya = 0
nizhnaya = 0
for i in range(n):
    for j in range(n):
     if (i > j) &  (i + j + 1 < n):
        levaya += int(s[i][j])
     if (i < j) & (i + j + 1 > n):
         pravaya += int(s[i][j])
     if (i < j) &  (i + j + 1 < n):
         verhnaya += int(s[i][j])
     if (i > j) &  (i + j + 1 > n):
         nizhnaya += int(s[i][j])
         
print ("Верхняя четверть: " + str(verhnaya) + '\n' + 
"Правая четверть: " + str(pravaya) + '\n' +
"Нижняя четверть: " + str(nizhnaya) + '\n' +
"Левая четверть: " + str(levaya))