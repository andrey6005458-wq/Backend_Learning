def max2D(matrix):
    return max(max(row) for row in matrix)


result = max2D([[-5, -43, 72, 89], [-40, 92, -1, -73], [30, -75, 23, 94]])
print(result)
