stroka = input().split()
n = len(stroka)
my_list = []
my_list.append([stroka[0]])
for i in range(1, n):
    if stroka[i] != stroka [i-1]:
        my_list.append([stroka[i]])
    else:
        my_list[-1].append(stroka[i])

print(my_list)