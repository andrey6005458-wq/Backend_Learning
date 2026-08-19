from itertools import permutations

n = int(input())
food = []

for _ in range(n):
    products = input().split(", ")
    food.extend(products)

for product in sorted(permutations(food, r=3)):
    print(*product)
