m = int(input())
n = int(input())
list1 = [input() for _ in range(m+n)]
set1 = set(list1)
s = len(list1) - ((len(list1)-len(set1))*2)
if s:
    print(s)
else:
    print('NO')