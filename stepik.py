n = int(input())
sl = {}
for i in range(n):
    key, value = input().split()
    sl[key] = value
    sl[value] = key
m = input()
print(sl[m])