n = int(input())
d = {}

for _ in range(n):
    text = input().replace(":", "").replace(",", "")
    parts = text.split()

    name = parts[0]  # имя ребёнка
    toys = parts[1:]  # список игрушек

    for toy in toys:
        if toy not in d:
            d[toy] = set()  # создаём множество для новой игрушки
        d[toy].add(name)  # добавляем имя ребёнка в множество

# Собираем игрушки, которые есть только у одного ребёнка
result = []
for toy, children in d.items():
    if len(children) == 1:
        result.append(toy)

# Выводим в алфавитном порядке
for toy in sorted(result):
    print(toy)
