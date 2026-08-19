count = 0
n = int(input())

for i in range(n):
    number = int(input())
    original = number
    reversed_num = 0

    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10

    if original == reversed_num:
        count += 1

print(count)
