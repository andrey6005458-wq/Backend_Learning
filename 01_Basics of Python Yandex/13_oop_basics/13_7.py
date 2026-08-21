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

    def get_pos(self):
        return (round(self.x, 2), round(self.y + self.height, 2))

    def get_size(self):
        return (round(self.width, 2), round(self.height, 2))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def resize(self, width, height):
        top_left_y = self.y + self.height
        self.width = width
        self.height = height
        self.y = top_left_y - height

    def turn(self):
        center_x = round(self.x + self.width / 2, 2)
        center_y = round(self.y + self.height / 2, 2)

        new_width = round(self.height, 2)
        new_height = round(self.width, 2)

        self.x = round(center_x - new_width / 2, 2)
        self.y = round(center_y - new_height / 2, 2)
        self.width = new_width
        self.height = new_height

    def scale(self, factor):
        center_x = round(self.x + self.width / 2, 2)
        center_y = round(self.y + self.height / 2, 2)

        self.width = round(self.width * factor, 2)
        self.height = round(self.height * factor, 2)

        self.x = round(center_x - self.width / 2, 2)
        self.y = round(center_y - self.height / 2, 2)

rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep='\n')