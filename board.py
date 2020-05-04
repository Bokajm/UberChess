import chessPiece
import king
import queen
import rook
import bishop
import knight
import pawn


class ChessBoard:
    actualBoard = [[]]

    def __init__(self, size=8):
        self.boardSize = size
        self.actualBoard = [[None for i in range(size)] for j in range(size)]

    # print the board (in console for now) if free - O, if occupied - color of the figure
    def showBoard(self):
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if self.actualBoard[i][j] is None:
                    print('O ', end='')
                else:
                    print(self.actualBoard[i][j].color + ' ', end='')
            print('')

    def clearBoard(self):
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                self.actualBoard[i][j] = None

    def defaultSetting(self):
        # pawns
        for i in range(self.boardSize):
            self.actualBoard[1][i] = pawn.Pawn(1,i,'B')
            self.actualBoard[self.boardSize-2][i] = pawn.Pawn(self.boardSize-2, i, 'W')
        # blacks
        self.actualBoard[0][0] = rook.Rook(0,0,'B')
        self.actualBoard[0][self.boardSize-1] = rook.Rook(0,self.boardSize-1,'B')
        self.actualBoard[0][1] = knight.Knight(0,1,'B')
        self.actualBoard[0][self.boardSize-2] = knight.Knight(0,self.boardSize-1,'B')
        self.actualBoard[0][2] = bishop.Bishop(0,2,'B')
        self.actualBoard[0][self.boardSize-3] = bishop.Bishop(0,self.boardSize-3,'B')

        # whites
        self.actualBoard[self.boardSize - 1][0] = rook.Rook(self.boardSize - 1, 0, 'W')
        self.actualBoard[self.boardSize - 1][self.boardSize - 1] = rook.Rook(self.boardSize - 1, self.boardSize - 1, 'W')
        self.actualBoard[self.boardSize - 1][1] = knight.Knight(self.boardSize - 1, 1, 'W')
        self.actualBoard[self.boardSize - 1][self.boardSize - 2] = knight.Knight(self.boardSize - 1, self.boardSize - 1, 'W')
        self.actualBoard[self.boardSize - 1][2] = bishop.Bishop(self.boardSize - 1, 2, 'W')
        self.actualBoard[self.boardSize - 1][self.boardSize - 3] = bishop.Bishop(self.boardSize - 1, self.boardSize - 3, 'W')


    # add a new chess piece to the board
    def addPiece(self, newPiece):
        x = newPiece.positionX
        y = newPiece.positionY
        if x < 0 or x >= self.boardSize or y < 0 or y >= self.boardSize:
            print('Not inside the board!')
        elif self.actualBoard[x][y] is not None:
            print('Occupied!')
        else:
            self.actualBoard[x][y] = newPiece

    def movePiece(self, piece, x, y):
        canMove = False
        for move in piece.availableMoves(self):
            if (x, y) == move:
                canMove = True

        if canMove:
            self.actualBoard[piece.positionX][piece.positionY] = None
            piece.positionX = x
            piece.positionY = y
            self.actualBoard[x][y] = piece
        else:
            print('Cannot move to that position!' + ' (' + str(x) + ', ' + str(y) + ')')

    # is the given position checked by given color
    def isCheckedBy(self, x, y, color):
        result = False
        if color != 'B' and color != 'W' and color != 'N':
            print('Wrong color!')
        else:
            for r in self.actualBoard:
                for piece in r:
                    if piece is not None:
                        if piece.color == color:
                            for move in piece.availableMoves(self):
                                if (x, y) == move:
                                    result = True
        return result



