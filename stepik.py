s = list(input())
m = list(input())
if len(s) != len(m):
    print('NO')
else:
    for i in range(len(s)):
        if s[i] in m:
            m.remove(s[i])
        else:
            print('NO')
    if len(m) == 0:
        print('YES')
