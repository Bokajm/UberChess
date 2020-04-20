import chessPiece

class King(chessPiece.ChessPiece):

    def availableMoves(self, board):
        moves = []

        for i in range(board.boardSize):
            for j in range(board.boardSize):
                if (board.actualBoard[i][j] == None or board.actualBoard[i][j].color != self.color):
                    if(abs(i-self.positionX) <= 1 and abs(j-self.positionY) <= 1):
                        moves.append((i, j))

        return moves