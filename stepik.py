m = input().split()
n = input().split()

set1 = set(m)
set2 = set(n)
set3 = set1 | set2
print(*sorted(set3))