import chessPiece


class Rook(chessPiece.ChessPiece):

    def availableMoves(self, board):
        moves = []

        for i in range(board.boardSize):
            for j in range(board.boardSize):
                if (board.actualBoard[i][j] == None or board.actualBoard[i][j].color != self.color):
                    if (i == self.positionX and j != self.positionY):
                        moves.append((i, j))
                    elif (i != self.positionX and j == self.positionY):
                        moves.append((i, j))

        return moves
