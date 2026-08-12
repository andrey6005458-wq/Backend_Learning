from itertools import chain

n = int(input())
products = []
for i in range(n):
    product = input().split(", ")
    products.append(product)
new_products = sorted(chain(*products))
for index, product in enumerate(new_products, 1):
    print(f"{index}. {(product)}")
