a = int(input())
b = int(input())
answer = [
    number**2 for number in range(a, b + (1 if a < b else -1), 1 if a < b else -1)
]
print(answer)
