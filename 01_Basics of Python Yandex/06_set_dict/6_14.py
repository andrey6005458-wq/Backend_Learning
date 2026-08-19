# 1. Вводим продукты, которые есть
n = int(input())
available = set()  # множество продуктов в наличии

for _ in range(n):
    product = input()
    available.add(product)

# 2. Вводим количество рецептов
m = int(input())
possible_dishes = []  # список блюд, которые можно приготовить

for _ in range(m):
    dish_name = input()  # название блюда
    count = int(input())  # количество ингредиентов
    ingredients = set()  # множество ингредиентов для этого блюда

    for _ in range(count):
        ingredient = input()
        ingredients.add(ingredient)

    # 3. Проверяем, есть ли все ингредиенты в наличии
    if ingredients.issubset(available):
        possible_dishes.append(dish_name)

# 4. Выводим результат
if possible_dishes:
    for dish in sorted(possible_dishes):
        print(dish)
else:
    print("Готовить нечего")
