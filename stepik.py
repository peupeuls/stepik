set1 = set(input().split())
set2 = set(input().split())
set3 = set1 & set2
if set3:
    print(*sorted(set3, reverse = True, key = int))
if not set3:
    print('BAD DAY')