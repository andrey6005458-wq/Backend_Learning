from itertools import product

n = int(input())
print("А", "Б", "В")
for a, b in product(range(1, n + 1), repeat=2):
    c = n - a - b
    if c >= 1:
        print(a, b, c)
