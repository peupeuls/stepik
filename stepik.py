m = int(input())
n = int(input())

set1 = {input() for _ in range(m)}
set2 = {input() for _ in range(n)}
set3 = set1 - set2
print(len(set3))