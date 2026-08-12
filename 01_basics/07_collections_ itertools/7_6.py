from itertools import product

nominal = [2, 3, 4, 5, 6, 7, 8, 9, 10, "валет", "дама", "король", "туз"]
suits = ["пик", "треф", "бубен", "червей"]

suits.remove(input())
for carts in product(nominal, suits):
    print(carts[0], carts[1])
