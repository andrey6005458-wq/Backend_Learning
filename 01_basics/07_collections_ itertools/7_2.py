a = input().split(", ")
b = input().split(", ")
for kids in zip(a, b):
    print(f"{kids[0]} - {kids[1]}")
