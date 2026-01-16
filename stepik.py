set1 = input().split()
set2 = input().split()
set3 = input().split()
set4 = set(set1) & set(set2) & set(set3)
set5 = (set(set1) | set(set2) | set(set3)) - set(set4)
for elem in sorted(set5, key = int):
    print(elem, end = " ")