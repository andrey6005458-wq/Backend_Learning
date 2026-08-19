numbers = [3, 1, 2, 3, 2, 2, 1]
answer = " - ".join(str(i) for i in sorted(set(numbers)))
print(answer)
