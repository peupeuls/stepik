s1 = input().split()

set1 = set(s1[0])
set2 = set(s1[1])
set3 = set(s1[2])

if set1 == set2 == set3:
    print("YES")
else:
    print("NO")