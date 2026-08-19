animal = 0
while (text := input()) != "Приехали!":
    if "зайка" in text:
        animal += 1

print(animal)
