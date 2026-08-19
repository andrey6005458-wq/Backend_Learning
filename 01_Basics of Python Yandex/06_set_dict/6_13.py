# Читаем общее количество блюд
n = int(input())
menu = set()

# Добавляем все возможные блюда
for _ in range(n):
    dish = input()
    menu.add(dish)

# Читаем количество дней
days = int(input())
cooked = set()

# Читаем блюда, приготовленные в каждый день
for _ in range(days):
    count = int(input())  # сколько блюд в этот день
    for _ in range(count):
        dish = input()
        cooked.add(dish)

# Находим блюда, которые НЕ готовили
leftovers = menu - cooked

# Выводим результат
if leftovers:
    for dish in sorted(leftovers):
        print(dish)
else:
    print("Готовить нечего")
