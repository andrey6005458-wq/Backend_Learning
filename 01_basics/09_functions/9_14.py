def can_eat(horse, other):
    x1, y1 = horse
    x2, y2 = other

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


result = can_eat((5, 5), (6, 6))
print(result)
