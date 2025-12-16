a = str(input())
letters = list(a)
b=len(letters)

sch = 0
maximum = 0
new_maximum = 0
for i in range (0, b):
        if letters[i] == "Р":
              sch += 1
              maximum = sch
              if new_maximum < maximum:
                new_maximum = maximum
        elif letters[i] == "О":
              sch = 0


print(new_maximum)