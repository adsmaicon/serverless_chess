"""[summary]

Returns:
    [type]: [description]
"""

class Piece:
    """[summary]
    """

    def __init__(self):
        """[summary]
        """
        self.codes = {
            'K': "King",
            "Q": "Queen",
            "R": "Rook",
            "B": "Bishop",
            "N": "Knight",
            "": "Pawn"
        }

    def code_validator(self, code):
        """[summary]

        Args:
            code ([type]): [description]

        Returns:
            [type]: [description]
        """
        return code.strip() in self.codes

    def position_validator(self, square):
        """
        docstring
        """
        return square
