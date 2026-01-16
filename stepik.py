n = input().split()
check = []
for i in range(len(n)):
    if int(n[i]) in check:
        print("YES")
    elif int(n[i]) not in check:
        print("NO")
    check.append(int(n[i]))


