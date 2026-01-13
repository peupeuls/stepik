n = int(input())
spisok = []
for i in range(n):
    spisok.append(input())

for i in range(n):
    print(spisok[i])
print()

for item in spisok:
    if '4' in item or '5' in item:
        print(item)