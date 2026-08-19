def answer(func):
    def new_func(*args, **kwargs):
        return f"Результат функции: {func(*args, **kwargs)}"

    return new_func


@answer
def a_plus_b(a, b):
    return a + b


print(a_plus_b(5, 10))
