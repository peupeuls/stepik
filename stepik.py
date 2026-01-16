n = input().split()
m = input().split()

set1 = set(n)
set2 = set(m)
set3 = set1 & set2
massiv = sorted(list(set3), key = int)
for elem in massiv:
    print(elem, end = " ")

