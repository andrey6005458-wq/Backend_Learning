def func(a, b):
    return a + b


try:
    func(None, None)
except TypeError:
    print('Ура! Ошибка!')
