h = int(input())
m = int(input())

max_number = h * m
width = len(str(max_number))

for i in range(h):
    for j in range(m):
        number = i + j * h + 1
        print(f"{number:>{width}}", end=" ")
    print()
