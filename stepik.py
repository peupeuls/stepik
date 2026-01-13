tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = []
n = len(tuples)
for i in range(n):
    a = list(tuples[i])
    a[-1] = 100
    b = tuple(a)
    new_tuples.append(b)
print(new_tuples)