# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip

from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, ROWS, COLS
from checkers.game import Game
from minimax.algorithm import minimax

class Calculator:

    def __init__(self,):
        self.FPS = 60

    def get_row_col_from_mouse(pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    def main(self, max_player):
        print('\nthe colour to move:', max_player, '\n')
        run = True
        game = Game()
        min_player = None
        if max_player == WHITE:
            min_player = RED
            print('\nmin player = RED\n')
        else:
            min_player = WHITE
            print('\nmin player = WHITE\n')


        value, new_board = minimax(game.get_board(), 4, max_player, game)
        move = self.strip_move(game.get_board().board, new_board.board, max_player)
        return move

    def strip_move(self, board, new_board, colour):
        taken = []
        moved_from = []
        moved_to = []

        same = True

        # iterate rows
        for row in range(ROWS):
            # iterate individual squares
            for col in range(COLS):
                piece = board[row][col]
                piece_new = new_board[row][col]
                # if it was empty, and now is filled with a piece of our colour - we have moved here
                if piece == 0 and piece_new != 0  and piece_new.color == colour:
                    moved_to.append([row, col])
                # if it used to hold our colour and now holds nothing, we started here
                if piece != 0  and piece.color == colour and piece_new == 0:
                    moved_from.append([row, col])
                # if it used to hold the other colour and now holds nothing, we took this piece
                if piece != 0 and piece.color != colour and piece_new == 0:
                    taken.append([row, col])
                    
        move = {"taken": taken, "moved_from": moved_from, "moved_to": moved_to}
        return move

    
