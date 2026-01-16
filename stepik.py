set1 = set(input())
set2 = set(input())
set3 = set1 & set2
if set3 == set2:
    print("YES")
else:
    print("NO")