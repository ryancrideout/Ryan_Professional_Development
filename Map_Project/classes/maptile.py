# from classes.abstract.character import Character

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
