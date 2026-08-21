class Cell:
    def __init__(self, status):
        self._status = status

    def status(self):
        return self._status


class Checkers:
    def __init__(self):
        self.board = []
        for row in range(8):
            current_row = []
            for col in range(8):
                if (row + col) % 2 == 0:  # Чёрные клетки
                    if row < 3:
                        status = "W"
                    elif row > 4:
                        status = "B"
                    else:
                        status = "X"
                else:
                    status = "X"
                current_row.append(Cell(status))
            self.board.append(current_row)

    def parse_position(self, position):
        col = ord(position[0]) - ord('A')
        row = int(position[1]) - 1
        return row, col

    def get_cell(self, position):
        row, col = self.parse_position(position)
        return self.board[row][col]

    def move(self, f, t):
        f_row, f_col = self.parse_position(f)
        t_row, t_col = self.parse_position(t)

        from_cell = self.board[f_row][f_col]
        to_cell = self.board[t_row][t_col]

        to_cell._status = from_cell._status
        from_cell._status = "X"

checkers = Checkers()
for row in '87654321':
    for col in 'ABCDEFGH':
        print(checkers.get_cell(col + row).status(), end='')
    print()