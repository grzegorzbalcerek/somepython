from color import Color
from enum import Enum, auto
    
class FigureType(Enum):
    """
    Represents chess figure types.
    """
    King = auto()
    Queen = auto()
    Rook = auto()
    Bishop = auto()
    Knight = auto()
    Pawn = auto()

class Figure:
    """
    Represents a figure, which has a type and a color.
    """

    def __init__(self, figure_type, figure_color):
        self.figure_type = figure_type
        self.figure_color = figure_color

    def __str__(self):
        """
        Returns a one-character string representing the figure.

        >>> print(Figure(FigureType.King, Color.White))
        k

        >>> print(Figure(FigureType.Queen, Color.White))
        q

        >>> print(Figure(FigureType.Rook, Color.White))
        r

        >>> print(Figure(FigureType.Bishop, Color.White))
        b

        >>> print(Figure(FigureType.Knight, Color.White))
        n

        >>> print(Figure(FigureType.Pawn, Color.White))
        p

        >>> print(Figure(FigureType.King, Color.Black))
        K

        >>> print(Figure(FigureType.Queen, Color.Black))
        Q

        >>> print(Figure(FigureType.Rook, Color.Black))
        R

        >>> print(Figure(FigureType.Bishop, Color.Black))
        B

        >>> print(Figure(FigureType.Knight, Color.Black))
        N

        >>> print(Figure(FigureType.Pawn, Color.Black))
        P
        """
        if   self.figure_type is FigureType.King   and self.figure_color is Color.White: return "k"
        elif self.figure_type is FigureType.Queen  and self.figure_color is Color.White: return "q"
        elif self.figure_type is FigureType.Rook   and self.figure_color is Color.White: return "r"
        elif self.figure_type is FigureType.Bishop and self.figure_color is Color.White: return "b"
        elif self.figure_type is FigureType.Knight and self.figure_color is Color.White: return "n"
        elif self.figure_type is FigureType.Pawn   and self.figure_color is Color.White: return "p"
        elif self.figure_type is FigureType.King   and self.figure_color is Color.Black: return "K"
        elif self.figure_type is FigureType.Queen  and self.figure_color is Color.Black: return "Q"
        elif self.figure_type is FigureType.Rook   and self.figure_color is Color.Black: return "R"
        elif self.figure_type is FigureType.Bishop and self.figure_color is Color.Black: return "B"
        elif self.figure_type is FigureType.Knight and self.figure_color is Color.Black: return "N"
        elif self.figure_type is FigureType.Pawn   and self.figure_color is Color.Black: return "P"

    def figure_symbol(self):
        """
        Returns a unicode symbol representing the figure.
        """
        if   self.figure_type is FigureType.King   and self.figure_color is Color.White: return "\u2654"
        elif self.figure_type is FigureType.Queen  and self.figure_color is Color.White: return "\u2655"
        elif self.figure_type is FigureType.Rook   and self.figure_color is Color.White: return "\u2656"
        elif self.figure_type is FigureType.Bishop and self.figure_color is Color.White: return "\u2657"
        elif self.figure_type is FigureType.Knight and self.figure_color is Color.White: return "\u2658"
        elif self.figure_type is FigureType.Pawn   and self.figure_color is Color.White: return "\u2659"
        elif self.figure_type is FigureType.King   and self.figure_color is Color.Black: return "\u265a"
        elif self.figure_type is FigureType.Queen  and self.figure_color is Color.Black: return "\u265b"
        elif self.figure_type is FigureType.Rook   and self.figure_color is Color.Black: return "\u265c"
        elif self.figure_type is FigureType.Bishop and self.figure_color is Color.Black: return "\u265d"
        elif self.figure_type is FigureType.Knight and self.figure_color is Color.Black: return "\u265e"
        elif self.figure_type is FigureType.Pawn   and self.figure_color is Color.Black: return "\u265f"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
