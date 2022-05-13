from classes.abstract.map import Map
from classes.maptile import MapTile

class Plain(Map):
    def __init__(self):
        self.width = None
        self.height = None
        self.grid = None

    def initialize(self, width, height):
        self.width = width
        self.height = height
        self.grid = {}
        for i in range(width):
            self.grid[i] = {}
            for j in range(height):
                # This is actually bad because it's using a specific class
                # and not an abstraction.
                self.grid[i][j] = MapTile()
                self.grid[i][j].set_coordinates(i, j)

    def render(self):
        """
        Coordinate numbers would be real nice to have, but that
        can be a strech goal and or come later.
        """
        if not self.grid:
            print("There is no map you display! AUGH!")
        else:
            for i in range(self.width):
                print(f"\n", end="")
                for j in range(self.height):
                    if self.grid[i][j].occupant:
                        print("|{}".format(self.grid[i][j].occupant.icon), end="")
                    else:
                        print("| ", end="")