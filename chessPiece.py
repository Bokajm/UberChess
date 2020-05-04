

class ChessPiece:
    # colors: W for white, B for black, N for neutral

    def __init__(self, x, y, color='N'):
        self.color = color
        self.positionX = x
        self.positionY = y
        self.moved = False

    def availableMoves(self, board):
        moves = []

        for i in range(board.boardSize):
            for j in range(board.boardSize):
                if (board.actualBoard[i][j] == None or board.actualBoard[i][j].color != self.color):
                    moves.append((i, j))

        return moves