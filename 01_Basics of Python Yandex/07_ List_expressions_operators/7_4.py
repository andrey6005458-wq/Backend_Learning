numbers = [1, 2, 3, 4, 5, 21, 32, 412]
answer = {number for number in numbers if number % 2}
print(*sorted(answer))
