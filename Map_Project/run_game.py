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

from classes.game import Game


UP = ["u", "up", "n", "north"]
DOWN = ["d", "down", "s", "south"]
LEFT = ["l", "left", "w", "west"]
RIGHT = ["r", "right", "e", "east"]


class Character(ABC):
  @abstractmethod
  def __init__(self):
      """
      I don't THINK we need the x and y but I included them anyways.
      """
      self.x = None
      self.y = None
      self.position = None

  @abstractmethod
  def set_position(self, x, y):
      self.position = (x, y)

  @abstractmethod
  def movement_action(self):
    """
    Not entirely satisfied with the name, but essentially the purpose
    of this method is to have a set of instructions for the game on
    how to move this character.
    """
    print("Shoryuken")


class Plebian(Character):
    def __init__(self):
        self.x = None
        self.y = None
        self.position = None

    def set_position(self, x, y):
        self.position = (x, y)

    def movement_action(self, direction):
        """
        Set of instructions on how Plebians move. Plebians
        don't have sophisticated movement, as demonstrated.
        """
        if direction.lower() in UP:
            return (self.x, (self.y + 1))
        elif direction.lower() in DOWN:
            return (self.x, (self.y - 1))
        elif direction.lower() in LEFT:
            return ((self.x - 1), self.y)
        elif direction.lower() in RIGHT:
            return ((self.x + 1), self.y)


# The main function where everything starts.
def main():
    map_game = Game()
    map_game.run()
    # Okay new plan - let the game handle movement, but the player classes will have instructions
    # on how to move.

# Actually run this blasted thing.
if __name__ == "__main__":
    main()