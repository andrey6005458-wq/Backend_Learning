def func(a, b, c):
    return ''.join(map(str, (a, b, c)))


class Broken:
    def __repr__(self):
        raise Exception


try:
    a = Broken()
    func(a)
except Exception:
    print('Ура! Ошибка!')