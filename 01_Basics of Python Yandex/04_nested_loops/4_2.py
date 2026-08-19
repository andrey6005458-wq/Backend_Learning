n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        answer = j * i
        print(f"{j} * {i} = {answer}")
