n = int(input())
m = int(input())

numbers = list(range(1, n * m + 1))

iters = [iter(numbers)] * m
rows = list(zip(*iters))

width = len(str(n * m))
for row in rows:
    for num in row:
        print(f"{num:>{width}}", end=" ")
    print()
