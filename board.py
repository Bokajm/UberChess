import  chessPiece

class ChessBoard:
    actualBoard = [[]]

    def __init__(self, size=8):
        self.boardSize = size
        self.actualBoard = [[None for i in range(size)] for j in range(size)]

    # print the board (in console for now) if free - O, if occupied - color of the figure
    def showBoard(self):
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if(self.actualBoard[i][j] == None):
                    print('O ', end='')
                else:
                    print(self.actualBoard[i][j].color + ' ', end='')
            print('')

    # add a new chess piece to the board
    def addPiece(self, newPiece):
        x = newPiece.positionX
        y = newPiece.positionY
        if(x < 0 or x >= self.boardSize or y < 0 or y >= self.boardSize):
            print('Not inside the board!')
        elif(self.actualBoard[x][y] != None):
            print('Occupied!')
        else:
            self.actualBoard[x][y] = newPiece

test = ChessBoard()
piece = chessPiece.ChessPiece(3,4)
piece2 = chessPiece.ChessPiece(0,0,'W')
test.addPiece(piece)
test.addPiece(piece2)

test.showBoard()

moves = piece.availableMoves(test)
print(moves)


