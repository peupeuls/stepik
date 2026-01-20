s = input().split()
new_s = []
for i in range(len(s)):
    new_s.append((s[i].lower()).strip('.,;:-?!()'))
r = {}
for w in new_s:
    if w not in r:
        r[w] = 1
    else:
        r[w] += 1

m = min(r.values())
n = []
for key in r.keys():
    if r[key] == m:
        n.append(key)
print(min(n))