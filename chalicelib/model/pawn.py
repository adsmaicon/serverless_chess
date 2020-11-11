
class Pawn:
    """
    docstring
    """
    def position_validator(self, origin, destination):
        return (origin is not None 
        and destination is not None
        and origin[0] == destination[0]        
        and int(destination[1]) - int(origin[1]) < 3)
