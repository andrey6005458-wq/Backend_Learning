def find_mountains(heights):
    mountains = []
    n = len(heights)
    for i in range(1, n - 1):
        if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
            mountains.append(i + 1)
    return tuple(mountains)


result = find_mountains([5, 1, 10, 2, 3, 4, 3, 20])
print(result)
