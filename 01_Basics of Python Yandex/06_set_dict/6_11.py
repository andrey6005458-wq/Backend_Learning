sum_mans = int(input())

same_surname = 0
d = {}

for surname in range(sum_mans):
    surnames = list(input())
    if surname in d:
        d.get("surname")
    else:
        d["surname"] = 1
        same_surname += 1
print(same_surname)
