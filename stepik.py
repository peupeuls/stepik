n = int(input())
slova = list()
sch = list()
for i in range (0, n):
    slova.append(str(input()))

b = len(slova)
for i in range (0, b):
    slovechko = list(slova[i])
    c = len(slovechko)
    found = False
    for j in range (0, c):
        if slovechko[j] == 'a':
            for k in range (j+1, c):
                if slovechko[k] == 'n':
                    for l in range (k+1, c):
                        if slovechko[l] == 't':
                            for m in range (l+1, c):
                                if slovechko[m] == 'o':
                                    for z in range (m+1, c):
                                        if slovechko[z] == 'n':
                                            sch.append(i+1)
                                            found = True
                                            break
                                    if found: break
                            if found: break
                    if found: break
        if found: break
result = " ".join(str(x) for x in sch)
print(result)
