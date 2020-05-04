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
                if (self.actualBoard[i][j] == None):
                    print('O ', end='')
                else:
                    print(self.actualBoard[i][j].color + ' ', end='')
            print('')

    # add a new chess piece to the board
    def addPiece(self, newPiece):
        x = newPiece.positionX
        y = newPiece.positionY
        if (x < 0 or x >= self.boardSize or y < 0 or y >= self.boardSize):
            print('Not inside the board!')
        elif (self.actualBoard[x][y] != None):
            print('Occupied!')
        else:
            self.actualBoard[x][y] = newPiece

    def movePiece(self, piece, x, y):
        canMove = False
        for move in piece.availableMoves(self):
            if ((x, y) == move):
                canMove = True

        if (canMove):
            self.actualBoard[piece.positionX][piece.positionY] = None
            piece.positionX = x
            piece.positionY = y
            self.actualBoard[x][y] = piece
        else:
            print('Cannot move to that position!' + ' (' + str(x) + ', ' + str(y) + ')')

    # is the given position checked by given color
    def isChecckedBy(self, x, y, color):
        result = False
        if(color != 'B' and color != 'W' and color != 'N'):
            print('Wrong color!')
        else:
            for r in self.actualBoard:
                for piece in r:
                    if(piece != None):
                        if(piece.color == color):
                            for move in piece.availableMoves(self):
                                if((x, y) == move):
                                    result = True
        return result





# do testów
test = ChessBoard()
pawn = pawn.Pawn(2,2,'B')
knight = knight.Knight(3,1,'W')
test.addPiece(pawn)
test.addPiece(knight)

test.showBoard()

moves = pawn.availableMoves(test)
print(moves)

