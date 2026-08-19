def get_repeater(func, count):
    def repeater(x):
        for _ in range(count):
            x = func(x)
        return x

    return repeater


repeater = get_repeater(lambda x: x * 2, 10)
print(repeater(1))
