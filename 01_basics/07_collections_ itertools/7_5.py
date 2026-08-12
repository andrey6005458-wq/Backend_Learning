from itertools import chain

products = []
for i in range(3):
    product = input().split(", ")
    products.append(product)
new_products = sorted(chain(*products))
for index, product in enumerate(new_products, 1):
    print(f"{index}. {(product)}")
