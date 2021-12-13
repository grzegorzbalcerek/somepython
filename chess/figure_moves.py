
from itertools import takewhile
from field import Field
from figure import Figure, FigureType
from color import Color

def rook_moves():
    """
    Sequences of relative figure positions for rook moves.

    >>> list(map(lambda x: (x[0][:4], x[1][:4]), rook_moves()))
    [([1, 2, 3, 4], [0, 0, 0, 0]), ([-1, -2, -3, -4], [0, 0, 0, 0]), ([0, 0, 0, 0], [1, 2, 3, 4]), ([0, 0, 0, 0], [-1, -2, -3, -4])]
    """
    return [
        (list(range(1,9)), list(x-x for x in range(9))),
        (list(range(-1,-9,-1)), list(x-x for x in range(9))),
        (list(x-x for x in range(9)), list(range(1,9))),
        (list(x-x for x in range(9)), list(range(-1,-9,-1)))
    ]


def bishop_moves():
    """
    Sequences of relative figure positions for bishop moves.

    >>> list(map(lambda x: (x[0][:4], x[1][:4]), bishop_moves()))
    [([1, 2, 3, 4], [1, 2, 3, 4]), ([-1, -2, -3, -4], [1, 2, 3, 4]), ([1, 2, 3, 4], [-1, -2, -3, -4]), ([-1, -2, -3, -4], [-1, -2, -3, -4])]
    """
    return [
        (list(range(1,9)), list(range(1,9))),
        (list(range(-1,-9,-1)), list(range(1,9))),
        (list(range(1,9)), list(range(-1,-9,-1))),
        (list(range(-1,-9,-1)), list(range(-1,-9,-1))),
     ]


def queen_moves():
    """
    Sequences of relative figure positions for queen moves.

    >>> list(map(lambda x: (x[0][:4], x[1][:4]), queen_moves()))
    [([1, 2, 3, 4], [0, 0, 0, 0]), ([-1, -2, -3, -4], [0, 0, 0, 0]), ([0, 0, 0, 0], [1, 2, 3, 4]), ([0, 0, 0, 0], [-1, -2, -3, -4]), ([1, 2, 3, 4], [1, 2, 3, 4]), ([-1, -2, -3, -4], [1, 2, 3, 4]), ([1, 2, 3, 4], [-1, -2, -3, -4]), ([-1, -2, -3, -4], [-1, -2, -3, -4])]
    """
    return rook_moves() + bishop_moves()


def knight_moves():
    """
    Sequences of relative figure positions for knight moves.
    """
    return [([1],[2]),([2],[1]),([-1],[2]),([2],[-1]),([-1],[-2]),([-2],[-1]),([1],[-2]),([-2],[1])]


def king_moves():
    """
    Sequences of relative figure positions for king moves.
    """
    return [([0],[1]),([0],[-1]),([1],[0]),([-1],[0]),([1],[1]),([-1],[-1]),([1],[-1]),([-1],[1])]


def choose_figure_moves(figure, field, capture):
    """
    Choose the sequences of relative figure positions
    based on the figure position, type, color,
    and whether the move is a capture move or not.

    >>> list(map(lambda x: (x[0][:4], x[1][:4]), choose_figure_moves(Figure(FigureType.Rook, Color.White), Field(4,5), True)))
    [([1, 2, 3, 4], [0, 0, 0, 0]), ([-1, -2, -3, -4], [0, 0, 0, 0]), ([0, 0, 0, 0], [1, 2, 3, 4]), ([0, 0, 0, 0], [-1, -2, -3, -4])]

    >>> choose_figure_moves(Figure(FigureType.Pawn, Color.White), Field(4,2), False)
    [([0, 0], [1, 2])]

    >>> choose_figure_moves(Figure(FigureType.Pawn, Color.Black), Field(4,7), False)
    [([0, 0], [-1, -2])]

    >>> choose_figure_moves(Figure(FigureType.Pawn, Color.Black), Field(4,5), False)
    [([0], [-1])]

    >>> choose_figure_moves(Figure(FigureType.Pawn, Color.White), Field(4,2), True)
    [([-1], [1]), ([1], [1])]

    >>> choose_figure_moves(Figure(FigureType.Pawn, Color.Black), Field(4,7), True)
    [([-1], [-1]), ([1], [-1])]
    """
    if figure.figure_type == FigureType.Rook:
        return rook_moves()
    elif figure.figure_type == FigureType.Bishop:
        return bishop_moves()
    elif figure.figure_type == FigureType.Queen:
        return queen_moves()
    elif figure.figure_type == FigureType.King:
        return king_moves()
    elif figure.figure_type == FigureType.Knight:
        return knight_moves()
    elif figure.figure_type == FigureType.Pawn:
        if capture:
            if figure.figure_color == Color.White:
                return [([-1],[1]),([1],[1])]
            elif figure.figure_color == Color.Black:
                return [([-1],[-1]),([1],[-1])]
        else:
            if figure.figure_color == Color.White:
                if field.row == 2:
                    return [([0,0],[1,2])]
                else:
                    return [([0],[1])]
            elif figure.figure_color == Color.Black:
                if field.row == 7:
                    return [([0,0],[-1,-2])]
                else:
                    return [([0],[-1])]


def relative_field(field, cr):
    """
    Returns the field relative to the given field according to
    a pair of relative coordinates.

    >>> print(relative_field(Field(1,2), (1,1)))
    b3

    >>> print(relative_field(Field(1,2), (0,2)))
    a4
    """
    return Field(field.col+cr[0], field.row+cr[1])


def relative_fields(field, cols_rows):
    """
    Returns fields relative to the given field according to
    the sequence of relative coordinates.

    >>> print(list(relative_fields(Field(2,2), ([1,2,3,4,5],[1,0,-1,-2,-3]))))
    [c3, d2, e1]
    """
    return list(takewhile(Field.is_valid, map(lambda x: relative_field(field,x), zip(cols_rows[0], cols_rows[1]))))


def figure_moves(figure, field, capture):
    """
    Returns possible figure moves.
    The figure is on the field 'field' and the 'capture' flag indicate whether
    the move is a capture.

    >>> figure_moves(Figure(FigureType.Rook, Color.White), Field(3, 4), False)
    [[d4, e4, f4, g4, h4], [b4, a4], [c5, c6, c7, c8], [c3, c2, c1]]

    >>> figure_moves(Figure(FigureType.Knight, Color.White), Field(2, 1), False)
    [[c3], [d2], [a3], [], [], [], [], []]

    >>> figure_moves(Figure(FigureType.Pawn, Color.White), Field(2, 2), False)
    [[b3, b4]]

    >>> figure_moves(Figure(FigureType.Pawn, Color.White), Field(2, 2), True)
    [[a3], [c3]]

    >>> figure_moves(Figure(FigureType.Pawn, Color.White), Field(1, 2), True)
    [[], [b3]]
    """
    return list(map(lambda x: relative_fields(field,x), choose_figure_moves(figure, field, capture)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
