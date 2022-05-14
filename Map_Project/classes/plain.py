from classes.abstract.map import Map
from classes.maptile import MapTile

class Plain(Map):
    def __init__(self):
        self.width = None
        self.height = None
        self.grid = None

    def initialize(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = {}
        for i in range(width):
            self.grid[i] = {}
            for j in range(height):
                self.grid[i][j] = MapTile()
                self.grid[i][j].set_coordinates(i, j)

    def render(self):
        """
        Coordinate numbers would be real nice to have, but that
        can be a strech goal and or come later.

        NOTE: Python prints to console from left to right, and from
              top to bottom. Traditional maps though, read left to
              right, bottom to top. As such, I've had to do with
              some monkeying around with the coordinates to make
              sure everything displays in an intuitive sense.
        """
        if not self.grid:
            print("There is no map you display! AUGH!")
        else:
            # TODO: Verify I got the width and height correct.
            #       I have my doubts.
            for i in range(self.height):
                y_index = self.height - 1 - i
                print(f"\n", end="")
                for x_index in range(self.width):
                    if self.grid[x_index][y_index].occupant:
                        print("|{}".format(self.grid[x_index][y_index].occupant.icon), end="")
                    else:
                        print("| ", end="")
                print("|", end="")
        print()