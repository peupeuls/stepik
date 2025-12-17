list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

total = 0
counter = 0
for sublist in list1:
    n = len(sublist)
    counter += n
    for i in range (0, n):
        total += sublist[i]
 
otvet=total/counter
print(otvet)
