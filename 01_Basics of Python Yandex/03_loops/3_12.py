number = int(input())
max_number = 0
while number > 0:
    max_number = max(max_number, number % 10)
    number //= 10
print(max_number)
