"""[summary]

Returns:
    [type]: [description]
"""
from chalicelib.model.pawn import Pawn
from chalicelib.model.king import King


class Piece:
    """[summary]
    """

    def __init__(self):
        """[summary]
        """
        self.codes = {
            'K': King(),
            "Q": "Queen",
            "R": "Rook",
            "B": "Bishop",
            "N": "Knight",
            "": Pawn()
        }

    def get_piece(self, code):
        return self.codes[code.strip()]

    def code_validator(self, code):
        """[summary]

        Args:
            code ([type]): [description]

        Returns:
            [type]: [description]
        """
        return code.strip() in self.codes

    def position_validator(self, oring, destination):
        """
        docstring
        """
        pass
