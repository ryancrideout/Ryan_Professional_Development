from classes.abstract.character import Character

class Jester(Character):
    def __init__(self):
        self.x = None
        self.y = None
        self.position = None
        self.icon = "J"

    def set_position(self, x: int, y: int):
        self.position = (x, y)
        self.x = x
        self.y = y

    def movement_action(self, direction: str):
        """
        The Jester has a little more chaotic movement, but
        only if people shake up their habits when it comes
        to typing out directions.

        Most programmers will think Jesters are identical
        to Plebians, haha.
        """
        tiles = len(direction)
        if direction.lower() in self.UP:
            return (self.x, (self.y + tiles))
        elif direction.lower() in self.DOWN:
            return (self.x, (self.y - tiles))
        elif direction.lower() in self.LEFT:
            return ((self.x - tiles), self.y)
        elif direction.lower() in self.RIGHT:
            return ((self.x + tiles), self.y)