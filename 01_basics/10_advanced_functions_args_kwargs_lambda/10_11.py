recipes = {
    "Эспрессо": {"coffee": 1},
    "Капучино": {"coffee": 1, "milk": 3},
    "Макиато": {"coffee": 2, "milk": 1},
    "Кофе по-венски": {"coffee": 1, "cream": 2},
    "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
    "Кон Панна": {"coffee": 1, "cream": 1},
}


def order(*args):
    for drink_name in args:
        if drink_name not in recipes:
            continue

        recipe = recipes[drink_name]

        enough = True
        for ingredient, amount in recipe.items():
            if in_stock.get(ingredient, 0) < amount:
                enough = False
                break

        if enough:
            for ingredient, amount in recipe.items():
                in_stock[ingredient] -= amount
            return f"Приготовлен напиток: {drink_name}"

    return f"К сожалению, не можем предложить Вам напиток {drink_name}"


in_stock = {"coffee": 4, "milk": 4, "cream": 4}
print(f"Остатки ингридиентов:")
for ingredient, amount in in_stock.items():
    print(f"{ingredient: <6}: {amount}шт.")
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Латте Макиато"))
print(f"Остатки ингридиентов:")
for ingredient, amount in in_stock.items():
    print(f"{ingredient: <6}: {amount}шт.")
