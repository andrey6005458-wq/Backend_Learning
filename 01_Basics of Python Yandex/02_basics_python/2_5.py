petya = 7
vasya = 6
n = int(input())
m = int(input())

petya1 = petya - 3 + 2 + n
vasya1 = vasya + 3 + 5 - 2 + m

if petya1 > vasya1:
    print('Петя')
else:
    print('Вася')