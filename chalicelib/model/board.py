

class Board:
    
    def __init__(self):
        self.square = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' ],
            [1, 2, 3, 4, 5, 6, 7, 8 ]
        ];

    
    def square_validator(self, square):
        return (square is not None 
        and len(square.strip()) == 2 
        and square[0].upper() in self.square[0]
        and int(square[1]) in self.square[1])