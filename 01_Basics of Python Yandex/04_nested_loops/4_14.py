h = int(input())
m = int(input())

width = len(str(h * m))

for i in range(h):
    for j in range(m):
        if i % 2 == 0:
            number = i * m + j + 1
        else:
            number = i * m + (m - j)
        print(f"{number:>{width}}", end=" ")
    print()
