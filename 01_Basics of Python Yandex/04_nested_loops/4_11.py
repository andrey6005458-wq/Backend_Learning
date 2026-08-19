n = int(input())
count = 0

for i in range(n):
    x = int(input())
    if x > 1:
        for divisor in range(2, round(x**0.5) + 1):
            if x % divisor == 0:
                break
        else:
            count += 1
print(count)
