n = int(input())
a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10
ansver = b * 1000 + a * 100 + d * 10 + c
print(ansver)
