class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, shift_x, shift_y):
        self.x += shift_x
        self.y += shift_y

    def length(self, p):
        return round(((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            x, y = 0, 0
        elif len(args) == 1:
            x, y = args[0]
        elif len(args) == 2:
            x, y = args[0], args[1]
        else:
            raise ValueError('Invalid number of arguments')
        super().__init__(x, y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'PatchedPoint({self.x}, {self.y})'

    def __add__(self, other):
        new_point = PatchedPoint(self.x + other[0], self.y + other[1])
        return new_point

    def __iadd__(self, other):
        self.move(other[0], other[1])
        return self

point = PatchedPoint()
print(point)
new_point = point + (2, -3)
print(point, new_point, point is new_point)