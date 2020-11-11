"""[summary]

Returns:
    [type]: [description]
"""

class Board:
    """[summary]
    """

    def __init__(self):
        """[summary]
        """
        self.square = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' ],
            [1, 2, 3, 4, 5, 6, 7, 8 ]
        ]

    def square_validator(self, square):
        """[summary]

        Args:
            square ([type]): [description]

        Returns:
            [type]: [description]
        """
        return (square is not None
        and len(square.strip()) == 2
        and square[0].upper() in self.square[0]
        and int(square[1]) in self.square[1])


    def position_validator(self, square):
        """
        docstring
        """
        return square
