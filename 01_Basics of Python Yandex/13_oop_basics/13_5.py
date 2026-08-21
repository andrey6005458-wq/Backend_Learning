class Rectangle:
    def __init__(self, first, second):
        x1, y1 = first
        x2, y2 = second

        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))

        self.x = x1
        self.y = y1
        self.width = x2 - x1
        self.height = y2 - y1

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def area(self):
        return round(self.width * self.height, 2)

rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())

rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())