from enum import Enum

class Color(Enum):
    """
    The `Color` class represents one of the two colors (`Black` or `White`)
    used in the game of Chess.
    """
    White = 1
    Black = 8

    def other(self):
        """
        Returns the opposite color.

        >>> Color.White.other()
        <Color.Black: 8>
        >>> Color.Black.other()
        <Color.White: 1>
        """
        if self == Color.White:
            return Color.Black
        elif self == Color.Black:
            return Color.White

    def first_row(self):
        """
        Returns the coordinate of the first row
        from the point of view of a player who plays the given color.

        >>> Color.White.first_row()
        1
        >>> Color.Black.first_row()
        8
        """
        return self.value

if __name__ == "__main__":
    import doctest
    doctest.testmod()

