h = int(input())
m = int(input())

width = len(str(h * m))

for i in range(h):
    for j in range(m):
        if j % 2 == 0:  # чётный столбец (0, 2, 4...) — сверху вниз
            number = i + j * h + 1
        else:  # нечётный столбец (1, 3, 5...) — снизу вверх
            number = (h - i - 1) + j * h + 1
        print(f"{number:>{width}}", end=" ")
    print()
