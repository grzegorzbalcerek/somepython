from enum import Enum, auto


class MoveType(Enum):
    RegularMove = auto()
    PromotionMove = auto()
    EnPassantMove = auto()
    CastlingMove = auto()


class Move:


    def __init__(self, type, frm, to, **data):
        self.type = type
        self.frm = frm
        self.to = to
        self.data = data

        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
