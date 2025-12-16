a = int(input())
numbers = []

da = False

for i in range (0, a):
    numbers.append(int(input()))

chislo = int(input())

for i in range (0, a):
    for j in range (i+1, a):
        if numbers[i] * numbers[j] == chislo:
            da = True

if da:
    print("ДА")
else: print("НЕТ")
