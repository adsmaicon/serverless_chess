

class Piece:
    
    def __init__(self):
        self.codes = {
            'K': "King",
            "Q": "Queen",
            "R": "Rook",
            "B": "Bishop",
            "N": "Knight",
            "": "Pawn"
        }
    
    def code_validator(self, code):
        return code.strip() in self.codes