numbers = [1, 2, 1, 3, 1, 2, 2, 4, 1, 2, 5, 1, 2]
answer = {num for num in numbers if numbers.count(num) == 1}
print(answer)
