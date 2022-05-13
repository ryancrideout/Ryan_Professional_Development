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
        plain = Plain()
        # Make this a user input
        plain.initialize(10, 10)
        # Yay this works
        plain.render()

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

class MapTile():
    """
    Future considerations for MapTiles:
    - Are they occupied?
    - Are there terrain effects?
    - Is it passible terrain?
    """
    @abstractmethod
    def __init__(self):
        self.x = None
        self.y = None
        self.coordinates = None
        self.occupant = None

    @abstractmethod
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = (x, y)

    @abstractmethod
    def set_occupant(self, occupant):
        # TODO - somehow force the "occupant" to be displayable.
        # I.E., occupant MUST have a ".icon".
        # Maybe do this later?
        self.occupant = occupant

# Unsure if we need this?
"""
class StandardMapTile(MapTile):
    
    # Note to self - I have code duplication here from the
    # MapTile class, but I figured I needed a map tile abstraction
    # for the initialization method. I don't know if I need this?
    
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
        self.occupant = occupant
"""

# The main function where everything starts.
def main():
    map_game = Game()
    map_game.run()
    # Should characters have a maptile object?
    # What about the map they're on?
    # Maybe I could just give them a "position" attribute...
    # But even so, moving them is going to require the map (maptiles plural) to be updated.
    # MAYBE I PUT "MOVE CHARACTERS" on the map command?
    # I think maybe we let the game handle all of that, and then it updates the map accordingly.
    # Ugh that's going to be messy.

    # Okay new plan - let the game handle movement, but the player classes will have instructions
    # on how to move.

# Actually run this blasted thing.
if __name__ == "__main__":
    main()