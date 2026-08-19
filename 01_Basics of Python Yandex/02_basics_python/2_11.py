number = int(input())
a = number // 100
b = number // 10 % 10
c = number % 10

# Находим минимальную, среднюю и максимальную цифры
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

# Теперь a — минимальная, b — средняя, c — максимальная
if a + c == b * 2:
    print("YES")
else:
    print("NO")
