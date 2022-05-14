from abc import ABC, abstractmethod

class Character(ABC):
    UP = ["u", "up", "n", "north"]
    DOWN = ["d", "down", "s", "south"]
    LEFT = ["l", "left", "w", "west"]
    RIGHT = ["r", "right", "e", "east"]

    @abstractmethod
    def __init__(self):
        """
        I don't THINK we need the x and y but I included them anyways.
        """
        self.x = None
        self.y = None
        self.position = None
        self.icon = "?"

    @abstractmethod
    def set_position(self, x, y):
        self.position = (x, y)
        self.x = x
        self.y = y

    @abstractmethod
    def movement_action(self):
      """
      Not entirely satisfied with the name, but essentially the purpose
      of this method is to have a set of instructions for the game on
      how to move this character.
      """
      print("This is how a character moves.")