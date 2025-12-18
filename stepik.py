def fact(n):
    a = 1
    if n == 0:
        return 1
    while n >= 1:
        a *= n
        n -= 1
    return int(a)


def paskal(n):
    c = []
    for k in range(n+1):
        c.append(str(fact(n)//(fact(k)*fact(n-k))))
    return c


n = int(input())
for i in range(n):
    print(' '.join(paskal(i)))