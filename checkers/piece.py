from .constants import RED, WHITE, SQUARE_SIZE, GREY

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color, king):
        self.row = row
        self.col = col
        self.color = color
        self.king = king
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)