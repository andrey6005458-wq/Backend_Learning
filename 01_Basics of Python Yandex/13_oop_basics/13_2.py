class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, shift_x, shift_y):
        self.x += shift_x
        self.y += shift_y

    def length(self, p):
        return round(((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5, 2)

point = Point(3, 5)
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)
first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))