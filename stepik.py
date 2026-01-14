n = int(input())
slova = []
for i in range(n):
    slova.append(input())


for i in range(n):
    m = len(set((slova[i]).lower()))
    print(m)
