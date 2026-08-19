numbers = {1, 2, 3, 4, 5}
answer = {num: [d for d in range(1, num + 1) if num % d == 0] for num in numbers}
print(answer)
