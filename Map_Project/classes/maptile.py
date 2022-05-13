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

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = (x, y)

    def set_occupant(self, occupant):
        # TODO - somehow force the "occupant" to be displayable.
        # I.E., occupant MUST have a ".icon".
        # Maybe do this later?
        self.occupant = occupant