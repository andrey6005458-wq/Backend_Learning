a = int(input())
b = int(input())

a1 = a // 100
a2 = (a // 10) % 10
a3 = a % 10

b1 = b // 100
b2 = (b // 10) % 10
b3 = b % 10

c1 = (a1 + b1) % 10
c2 = (a2 + b2) % 10
c3 = (a3 + b3) % 10

result = c1 * 100 + c2 * 10 + c3
print(result)
