n = int(input())
sl = {}
for i in range(n):
    key, value = input().split(': ')
    sl[key.lower()] = value
m = int(input())
for i in range(m):
    slovo = input().lower()
    s = sl.get(slovo, 'Не найдено')
    print(s)