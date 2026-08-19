product = input()
price = int(input())
weight = int(input())
money = int(input())
total = price * weight
change = money - total
print("Чек")
print(f"{product} - {weight}кг - {price}руб/кг")
print(f"Итого: {total}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {change}руб")
