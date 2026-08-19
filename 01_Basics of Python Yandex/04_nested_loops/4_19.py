N = int(input())

# Вычисляем ширину столбца по количеству цифр в центральном числе
width = len(str((N + 1) // 2))

for row in range(N):
    line = []
    for col in range(N):
        number = min(row + 1, col + 1, N - row, N - col)
        line.append(f"{number:>{width}}")  # выравниваем по правому краю по ширине
    print(" ".join(line))
