"""
Things to do:
- Create a Game Class
- Create an abstract Map Class
  - Make a "Plain" Subsclass
- Create a MapTile Class
- Create an abstract Character Class
  - Make some character classes
- Cleanup, put these into folders and stuff.
"""

from abc import ABC, abstractmethod

class Game():
    def run(self):
        """
        Okay we're going to have to figure out how to initialize this whole thing...
        But that's a problem for later?
        """
        # Make a plain. We can implement logic later to choose our map type.

class Map(ABC):
    @abstractmethod
    def __init__(self):
        self.width = None
        self.height = None
        self.grid = None

    @abstractmethod
    def initialize(self, width, height):
        print("MAKE A MAP YOU FOOL")

    @abstractmethod
    def render(self):
        print("We're going to have to print out the map here.")

class Plain(Map):
    def __init__(self):
        self.width = None
        self.height = None
        self.grid = None

    def initialize(self, width, height):
        self.width = width
        self.height = height
        # Fill out the grid; I'm thinking a dictionary of dictionaries that each
        # have a map tile.
        print("Hi yes I'm a Plain.")

    def render(self):
        print("This actually prints the map, you FOOL.")

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

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = (x, y)

# The main function where everything starts.
def main():
    map_game = Game()
    map_game.run()

# Actually run this blasted thing.
if __name__ == "__main__":
    main()