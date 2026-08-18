def gcd(*args):
    # Защита от пустого вызова
    if not args:
        return 0

    # Преобразуем кортеж в список, чтобы можно было изменять
    numbers = list(args)

    # Пока в списке больше одного числа
    while len(numbers) > 1:
        # Берем первые два числа
        a, b = numbers[0], numbers[1]

        # Вычисляем их НОД (алгоритм Евклида)
        while b != 0:
            a, b = b, a % b

        # Заменяем первые два числа на их НОД
        numbers = [a] + numbers[2:]

    # Возвращаем единственное оставшееся число
    return numbers[0]


# Проверка
print(gcd(36, 48, 156, 100500))  # 12
print(gcd(10, 20, 30))  # 10
print(gcd(7, 13))  # 1
print(gcd(100))  # 100
print(gcd())  # 0
print(gcd())  # 0
