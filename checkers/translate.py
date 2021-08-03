import math
from yolov5.detect import Detect

class Translate:
    WIDTH, HEIGHT = 800, 800
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)

    def __init__(self):
        # Classes:
        # 0 Black
        # 1 Black King
        # 2 Bottom Left
        # 3 Bottom Right
        # 4 Top Left
        # 5 Top Right
        # 6 White
        # 7 White King

 #       with open("labels.txt", 'r') as fobj:
  #          self.labels = [[float(num) for num in line.split()] for line in fobj]
   ##     for label in self.labels:
#            label[0] = (int)(label[0])

        detector = Detect()
        results = detector.detect()
        self.labels = [[float(num) for num in line.split()] for line in results]
        for label in self.labels:
            label[0] = (int)(label[0])
#        self.boxes = []
 #       for result in results:
  #          box = []
   #         for i in range(len(box)):
    #            if i == 0:
     #               box.append(int(result[i]))
      #          else:
       #             box.append(float(result[i]))
        #    self.boxes.append(box)
#        print('\n\n' + 'self.boxes:')
 #       print(self.boxes)

        self.pieces = []
        self.black = []
        self.white = []
        self.black_king = []
        self.white_king = []
        self.bottom_left = []
        self.bottom_right = []
        self.top_left = []
        self.top_right = []
        self.board = []

        # categorize labels
        for label in self.labels:
            if label[0] == 0 or label[0] == 1 or label[0] == 6 or label[0] == 7:
                self.pieces.append(label)
            elif label[0] == 2:
                self.bottom_left.append(label)
                if len(self.bottom_left) > 1:
                    print('too many corners detected')
                    exit(1)
            elif label[0] == 3:
                self.bottom_right.append(label)
                if len(self.bottom_right) > 1:
                    print('too many corners detected')
                    exit(1)
            elif label[0] == 4:
                self.top_left.append(label)
                if len(self.top_left) > 1:
                    print('too many corners detected')
                    exit(1)
            elif label[0] == 5:
                self.top_right.append(label)
                if len(self.top_right) > 1:
                    print('too many corners detected')
                    exit(1)

            # Check for more than one of each corner and throw error if so - TODO

        self.bottom_left = self.bottom_left[0]
        self.bottom_right = self.bottom_right[0]
        self.top_left = self.top_left[0]
        self.top_right = self.top_right[0]

        # define valid squares for plotting
        self.valid_sqaures = [1, 3, 5, 7, 8, 10, 12, 14, 17, 19, 21, 23, 24, 26, 28, 30, 33, 35, 37, 39, 40, 42, 44, 46, 49, 51, 53, 55, 56, 58, 60, 62]


    def translate_board(self):
        self.create_board (self.board, self.top_left, self.top_right, self.bottom_left, self.bottom_right)
        pieces = self.plot_pieces(self.pieces, self.board)
        return pieces

    # starting from the left x,y - find all squares in the row to the right x,y
    def plot_line(self, start, end):
        # line of x,y values
        line = []
        
        # horizontal and vertical gaps to cross
        horizontal = end[0] - start[0]
        vertical = end[1] - start[1]

        # x,y distances for each square
        x_increment = horizontal / 7
        y_increment = vertical / 7 

        # variable to hold x,y values of squares as iterated
        square = [start[0], start[1]]

        # iterate x,y values for row and add to table
        for i in range(7):
            square[0] += x_increment
            square[1] += y_increment
            x = square[0]
            y = square[1]
            line.append([x, y])
        return line


    def create_board(self, board, top_left, top_right, bottom_left, bottom_right):
        # x, y, index
        board.append([top_left[1], top_left[2]])

        # find left edge squares
        left_edge = self.plot_line([top_left[1], top_left[2]], [bottom_left[1], bottom_left[2]])
        right_edge = self.plot_line([top_right[1], top_right[2]], [bottom_right[1], bottom_right[2]])

        # create top line
        for item in self.plot_line([top_left[1], top_left[2]], [top_right[1], top_right[2]]):
            board.append(item)

        for i in range(7):
            board.append(left_edge[i])
            for item in self.plot_line(left_edge[i], right_edge[i]):
                board.append(item)
        

    # just checks for closest square, doesn't currently account for pieces detected off the board
    # returns the board index of the piece
    def plot_piece(self, piece, board):
        min_dist = 1000000
        place = -1
        for i in range(64) :
            x_dist = piece[1] - board[i][0]
            if x_dist < 0:
                x_dist *= -1

            y_dist = piece[2] - board[i][1]
            if y_dist < 0:
                y_dist *= -1

            dist = math.sqrt((x_dist ** 2) + (y_dist ** 2))
            if dist < min_dist and i in self.valid_sqaures:
                min_dist = dist
                place = i

        return place

    def assert_kings(self):
        # for every piece
        for piece1 in self.board_locations:
            # check against every piece
            for piece2 in self.board_locations:
                # for the same position (omitting checking itself)
                if piece1[1] == piece2[1] and piece1[0] != piece2[0]:
                    if piece1[0] != 1 or piece1[0] != 7:
                        self.board_locations.remove(piece1)
                    elif piece2[0] != 1 or piece2[0] != 7:
                        self.board_locations.remove(piece2)

            
    def plot_pieces(self, pieces, board):
        self.board_locations = []
        for piece in pieces:
            piece_type = piece[0]
            piece_index = self.plot_piece(piece, board)
            self.board_locations.append([piece_type, piece_index])
        self.assert_kings()
        return self.board_locations