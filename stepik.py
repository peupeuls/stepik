s1 = input()
s2 = input()
total = s1 + s2
flag = True
for i in range(10):
    if str(i) not in total:
        flag = False

if flag:
    print("YES")
else:
    print("NO")