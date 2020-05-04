

import board
import chessPiece
import king
import queen
import rook
import bishop
import knight
import pawn


# do testów
test = board.ChessBoard()
pawn1 = pawn.Pawn(2, 2, 'B')
pawn2 = pawn.Pawn(2, 3, 'B')
knight1 = knight.Knight(3, 1, 'W')
#knight2 = knight.Knight(4, 5, 'W')
test.addPiece(pawn1)
test.addPiece(pawn2)
test.addPiece(knight1)
#test.addPiece(knight2)

test.showBoard()

moves = pawn1.availableMoves(test)
print(moves)

test.clearBoard()
test.defaultSetting()

test.showBoard()