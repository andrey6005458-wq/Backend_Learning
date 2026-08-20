def same_type(func):
    def wrapper(*args):
        if len({type(i) for i in args}) != 1:
            print("Обнаружены различные типы данных")
            return False
        return func(*args)

    return wrapper


@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or "Fail")
print(a_plus_b(7, "9") or "Fail")
print(a_plus_b(-3, 5) or "Fail")
