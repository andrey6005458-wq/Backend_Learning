n = int(input())
result = 0

for i in range(n):
    max_digit = 0
    x = int(input())
    while x > 0:
        max_digit = max(max_digit, x % 10)
        x //= 10
    result = max_digit + (result * 10)

print(result)
