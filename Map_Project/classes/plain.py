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
