
def chunked():
    stroka = input().split()
    m = int(input())
    n = len(stroka)
    my_list = []
    my_list.append([stroka[0]])
    for i in range(1, n):
        if i % m != 0:
            my_list[-1].append(stroka[i])
        else:
            my_list.append([stroka[i]])
    print(my_list)
chunked()