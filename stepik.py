# n = set(input().replace(' ', ''))
# m = set(input().replace(' ', ''))

# s = n & m
# print(s)
n = (input().lower()).split()
s = set()
for i in range(len(n)):
    new_n = n[i].strip('.,;:-?!')
    s.add(new_n)

print(len(s))
