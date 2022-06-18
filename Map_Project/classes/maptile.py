from classes.abstract.character import Character

class MapTile():
    """
    Future considerations for MapTiles:
    - Are they occupied?
    - Are there terrain effects?
    - Is it passible terrain?
    """
    def __init__(self):
        self.x = None
        self.y = None
        self.coordinates = None
        self.occupant = None

    def set_coordinates(self, x: int, y: int):
        # We're casting to integer here so that we can catch bad inputs
        # should they happen.
        self.x = int(x)
        self.y = int(y)
        self.coordinates = (int(x), int(y))

    def set_occupant(self, occupant: Character):
        # RE: Type Checking - while I enforce the occupant to be a character,
        #     I could foresee other "entity" types occupying a map space.
        if occupant == None:
            self.occupant = occupant
        elif not isinstance(occupant, Character):
            raise TypeError("Cannot make a non-character a map occupant!")
        else:
            self.occupant = occupant