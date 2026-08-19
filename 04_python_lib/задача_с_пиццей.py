a, b, c = map(int, input().split())
every = (a + (c / 100 * a))/b
print(f'Каждый платит: {int(every)} руб.')