n = int(input())
slova = []
for i in range(n):
    slova.append(input())
vmeste = ''.join(slova)
s = len(set(vmeste.lower()))
print(s)
