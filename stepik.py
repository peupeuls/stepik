
s = input().split()
n = len(s)
sublist = [[]]
for i in range(n):
   for j in range(n):
         if s[i:j+1]:
              sublist.append(s[i:j+1])
print(sublist)


         
      