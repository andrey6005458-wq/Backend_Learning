number = int(input())
new_number = 0
place = 1

while number > 0:
    digit = number % 10
    if digit % 2 != 0:
        new_number += digit * place
        place *= 10
    number //= 10

print(new_number)
