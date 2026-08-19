a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

buy1 = a - (b / 100 * a)
buy2 = c - (d / 100 * c)
buy3 = e - (f / 100 * e)
answer = buy1 + buy2 + buy3

print(f'С учетом скидки вы потратите: {int(answer)}')