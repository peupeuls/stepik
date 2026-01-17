n = int(input())
list1 = [input() for _ in range(n+1)]
set1 = set(list1)
if len(list1) == len(set1):
    print('OK')
else:
    print('REPEAT')