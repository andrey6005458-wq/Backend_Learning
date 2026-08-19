numbers = {1, 2, 3, 4, 5}
answer = max(x * y for x in numbers for y in numbers if x != y)
print(answer)
