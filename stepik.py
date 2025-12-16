n = int(input())
slova = list()
sch = list()
for i in range (0, n):
    slova.append(str(input()))

b = len(slova)
for i in range (0, b):
    if 'a' in slova[i]:
        if 'n' in slova[i]:
            if 't' in slova[i]:
                if 'o' in slova[i]:
                    if 'n' in slova[i]:
                        sch.append(i+1)

result = " ".join(str(x) for x in sch)
print(result)
