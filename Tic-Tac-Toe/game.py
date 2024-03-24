
X_PIECE = 'X'
O_PIECE = 'O'
EMPTY_PIECE = ' '

class Game:
    def __init__(self):
        self.board = [[EMPTY_PIECE for _ in range(3)] for _ in range(3)]
        self.xTurn = True

    def is_x_turn(self):
        return self.xTurn

    def move(self, r, c):
        if self.board[r][c] != EMPTY_PIECE:
            return False

        if self.xTurn:
            self.board[r][c] = X_PIECE
        else:
            self.board[r][c] = O_PIECE

        self.xTurn = not self.xTurn
        return True

    def print(self):
        for row in self.board:
            print(row)

    def check_win(self):
        # columns
        w0 = self.check(0, 0, 0, 1)
        if w0 != EMPTY_PIECE:
            return w0
        w1 = self.check(0, 1, 0, 1)
        if w1 != EMPTY_PIECE:
            return w1
        w2 = self.check(0, 2, 0, 1)
        if w2 != EMPTY_PIECE:
            return w2

        # rows
        w3 = self.check(0, 0, 1, 0)
        if w3 != EMPTY_PIECE:
            return w3
        w4 = self.check(1, 0, 1, 0)
        if w4 != EMPTY_PIECE:
            return w4
        w5 = self.check(2, 0, 1, 0)
        if w5 != EMPTY_PIECE:
            return w5

        # crosses
        w6 = self.check(0, 0, 1, 1)
        if w6 != EMPTY_PIECE:
            return w6
        w7 = self.check(0, 2, 1, -1)
        if w7 != EMPTY_PIECE:
            return w7

    def check(self, ix, iy, dx, dy):
        if self.board[ix][iy] == EMPTY_PIECE:
            return EMPTY_PIECE
        temp = self.board[ix][iy]
        for _ in range(2):
            ix += dx
            iy += dy
            if temp != self.board[ix][iy]:
                return EMPTY_PIECE
        return temp
