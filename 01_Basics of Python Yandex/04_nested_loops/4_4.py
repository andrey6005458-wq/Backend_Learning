n = int(input())
summ = 0

for i in range(n):
    x = int(input())
    while x > 0:
        summ += x % 10
        x //= 10
print(summ)
