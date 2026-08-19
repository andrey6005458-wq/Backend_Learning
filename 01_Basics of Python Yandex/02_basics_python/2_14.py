numeros = int(input())

a = numeros // 100
b = numeros // 10 % 10
c = numeros % 10

# a - min, b - mid, c - max
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

if a == 0:
    print(f"{b}{a} {c}{b}")
else:
    print(f"{a}{b} {c}{b}")
