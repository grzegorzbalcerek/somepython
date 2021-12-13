from color import Color
from figure import Figure, FigureType
from field import Field
from move import Move, MoveType

def starting_board():
    return {
        (1,1): Figure(FigureType.Rook, Color.White),
        (2,1): Figure(FigureType.Knight, Color.White),
        (3,1): Figure(FigureType.Bishop, Color.White),
        (4,1): Figure(FigureType.Queen, Color.White),
        (5,1): Figure(FigureType.King, Color.White),
        (6,1): Figure(FigureType.Bishop, Color.White),
        (7,1): Figure(FigureType.Knight, Color.White),
        (8,1): Figure(FigureType.Rook, Color.White),
        (1,2): Figure(FigureType.Pawn, Color.White),
        (2,2): Figure(FigureType.Pawn, Color.White),
        (3,2): Figure(FigureType.Pawn, Color.White),
        (4,2): Figure(FigureType.Pawn, Color.White),
        (5,2): Figure(FigureType.Pawn, Color.White),
        (6,2): Figure(FigureType.Pawn, Color.White),
        (7,2): Figure(FigureType.Pawn, Color.White),
        (8,2): Figure(FigureType.Pawn, Color.White),
        (1,7): Figure(FigureType.Pawn, Color.Black),
        (2,7): Figure(FigureType.Pawn, Color.Black),
        (3,7): Figure(FigureType.Pawn, Color.Black),
        (4,7): Figure(FigureType.Pawn, Color.Black),
        (5,7): Figure(FigureType.Pawn, Color.Black),
        (6,7): Figure(FigureType.Pawn, Color.Black),
        (7,7): Figure(FigureType.Pawn, Color.Black),
        (8,7): Figure(FigureType.Pawn, Color.Black),
        (1,8): Figure(FigureType.Rook, Color.Black),
        (2,8): Figure(FigureType.Knight, Color.Black),
        (3,8): Figure(FigureType.Bishop, Color.Black),
        (4,8): Figure(FigureType.Queen, Color.Black),
        (5,8): Figure(FigureType.King, Color.Black),
        (6,8): Figure(FigureType.Bishop, Color.Black),
        (7,8): Figure(FigureType.Knight, Color.Black),
        (8,8): Figure(FigureType.Rook, Color.Black)
    }

def show_board(board):
    """
    Shows the board.

    >>> print(show_board(starting_board()))
     abcdefgh
    8RNBQKBNR8
    7PPPPPPPP7
    6........6
    5........5
    4........4
    3........3
    2pppppppp2
    1rnbqkbnr1
     abcdefgh
    """
    def row_to_str(row):
        return "".join([str(board.get((col,row), ".")) for col in range(1,9)])
    return (" abcdefgh\n" +
            "".join([ (str(row) + row_to_str(row) + str(row) + "\n") for row in range(8,0,-1)]) +
            " abcdefgh")


def update_board(board, move):
    """
    Returns a new board, updated with a move.

    >>> print(show_board(update_board(starting_board(), Move(MoveType.RegularMove, Field(2,2), Field(2,3)))))
     abcdefgh
    8RNBQKBNR8
    7PPPPPPPP7
    6........6
    5........5
    4........4
    3.p......3
    2p.pppppp2
    1rnbqkbnr1
     abcdefgh

    >>> print(show_board(update_board(starting_board(), Move(MoveType.RegularMove, Field(3,3), Field(2,3)))))
     abcdefgh
    8RNBQKBNR8
    7PPPPPPPP7
    6........6
    5........5
    4........4
    3........3
    2pppppppp2
    1rnbqkbnr1
     abcdefgh

    >>> print(show_board(update_board(starting_board(), Move(MoveType.PromotionMove, Field(2,2), Field(2,8), figure=Figure(FigureType.Queen, Color.White)))))
     abcdefgh
    8RqBQKBNR8
    7PPPPPPPP7
    6........6
    5........5
    4........4
    3........3
    2p.pppppp2
    1rnbqkbnr1
     abcdefgh

    >>> print(show_board(update_board(starting_board(), Move(MoveType.EnPassantMove, Field(2,2), Field(3,3), captured=Field(3,7)))))
     abcdefgh
    8RNBQKBNR8
    7PP.PPPPP7
    6........6
    5........5
    4........4
    3..p.....3
    2p.pppppp2
    1rnbqkbnr1
     abcdefgh

    >>> print(show_board(update_board(starting_board(), Move(MoveType.CastlingMove, Field(5,1), Field(3,1), rook_from=Field(1,1), rook_to=Field(4,1)))))
     abcdefgh
    8RNBQKBNR8
    7PPPPPPPP7
    6........6
    5........5
    4........4
    3........3
    2pppppppp2
    1.nkr.bnr1
     abcdefgh
    """
    from_key = (move.frm.col, move.frm.row)
    to_key = (move.to.col, move.to.row)
    if move.type == MoveType.RegularMove:
        if (from_key in board):
            new_board = board.copy()
            new_board[to_key] = new_board[from_key]
            del new_board[from_key]
            return new_board
        else:
            return board.copy()
    elif move.type == MoveType.PromotionMove:
        if (from_key in board):
            new_board = board.copy()
            new_board[to_key] = move.data['figure']
            del new_board[from_key]
            return new_board
        else:
            return board.copy()
    elif move.type == MoveType.EnPassantMove:
        if (from_key in board):
            captured_key = (move.data['captured'].col, move.data['captured'].row)
            new_board = board.copy()
            new_board[to_key] = new_board[from_key]
            del new_board[from_key]
            del new_board[captured_key]
            return new_board
        else:
            return board.copy()
    elif move.type == MoveType.CastlingMove:
        rook_from_key = (move.data['rook_from'].col, move.data['rook_from'].row)
        if (from_key in board and rook_from_key in board):
            rook_to_key = (move.data['rook_to'].col, move.data['rook_to'].row)
            new_board = board.copy()
            new_board[to_key] = new_board[from_key]
            new_board[rook_to_key] = new_board[rook_from_key]
            del new_board[from_key]
            del new_board[rook_from_key]
            return new_board
        else:
            return board.copy()


if __name__ == "__main__":
    import doctest
    doctest.testmod()

