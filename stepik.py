set1 = input().split()
set2 = input().split()
set3 = input().split()
set4 = set(set1) & set(set2)
set5 = set(set4) - set(set3)
for elem in sorted(set5, reverse=True, key = int):
    print(elem, end = " ")