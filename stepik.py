stroka = input().split()
n = int(input())
dlina = len(stroka)

result = []
i = 0
while i < n:
   result.append(stroka[i::n])
   i += 1
print(result)
