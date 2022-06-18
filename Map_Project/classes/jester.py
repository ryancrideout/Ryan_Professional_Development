from classes.abstract.character import Character

class Jester(Character):
    def __init__(self):
        self.x = None
        self.y = None
        self.position = None
        self.icon = "J"
        self.name = None

    def set_position(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)
        self.position = (int(x), int(y))

    def set_name(self, name: str):
        self.name = str(name)

    def movement_action(self, direction: str):
        """
        The Jester has a little more chaotic movement, but
        only if people shake up their habits when it comes
        to typing out directions.

        Most programmers will think Jesters are identical
        to Plebians, haha.
        """
        if (self.x == None) or (self.y == None):
            raise ValueError("Missing an X or Y (or both, heh) value!")

        tiles = len(direction)
        if direction.lower() in self.UP:
            return (self.x, (self.y + tiles))
        elif direction.lower() in self.DOWN:
            return (self.x, (self.y - tiles))
        elif direction.lower() in self.LEFT:
            return ((self.x - tiles), self.y)
        elif direction.lower() in self.RIGHT:
            return ((self.x + tiles), self.y)
        else:
            print("Error! Direction not recognized. Not moving {}.".format(self.name))
            return (self.x, self.y)