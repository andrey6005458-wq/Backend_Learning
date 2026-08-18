def grow(*args, **kwargs):
    contributions = [0] * len(args)

    for key, value in kwargs.items():
        key_len = len(key)
        if key_len == 0:
            continue

        for i in range(len(args)):
            if args[i] % key_len == 0:
                contributions[i] += value
    result = tuple(args[i] + contributions[i] for i in range(len(args)))

    return result


# Проверка
print(grow(1, 2, 3, 4, 5, ab=7, dad=10))  # (1, 9, 13, 11, 5)
print(grow(12, 5, 30, 60, 15, first=13, second=2, Bob=7))
