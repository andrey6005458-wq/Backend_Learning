def find_mountains(data):
    rows = len(data)
    cols = len(data[0])
    result = []

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            current = data[i][j]
            is_peak = True

            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0:
                        continue
                    if current <= data[i + di][j + dj]:
                        is_peak = False
                        break
                if not is_peak:
                    break

            if is_peak:
                result.append((i + 1, j + 1))

    return tuple(result)


result = find_mountains(
    [
        [1, 1, 1, 1, 1, 1],
        [1, 2, 1, 5, 4, 1],
        [1, 1, 1, 3, 4, 3],
        [2, 3, 3, 1, 2, 3],
        [1, 2, 1, 3, 2, 1],
    ]
)
print(result)
