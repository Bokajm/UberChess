import chessPiece

class Pawn(chessPiece.ChessPiece):

    def availableMoves(self, board):
        moves = []

        for i in range(board.boardSize):
            for j in range(board.boardSize):
                if (board.actualBoard[i][j] == None or board.actualBoard[i][j].color != self.color):
                    if(self.color == 'W'):
                        if(i == self.positionX - 1 and j == self.positionY):
                            moves.append((i, j))
                        if(board.actualBoard[i][j] != None):
                            if(i == self.positionX - 1 and abs(j - self.positionY) == 1 and board.actualBoard[i][j].color == 'B'):
                                moves.append((i, j))
                    if (self.color == 'B'):
                        if (i == self.positionX + 1 and j == self.positionY):
                            moves.append((i, j))
                        if(board.actualBoard[i][j] != None):
                            if (i == self.positionX + 1 and abs(j - self.positionY) == 1 and board.actualBoard[i][j].color == 'W'):
                                moves.append((i, j))
        return moves