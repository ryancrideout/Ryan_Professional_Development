from classes.abstract.character import Character

class Plebian(Character):
    def __init__(self):
        self.x = None
        self.y = None
        self.position = None
        self.icon = "P"

    def set_position(self, x: int, y: int):
        self.position = (x, y)
        self.x = x
        self.y = y

    def movement_action(self, direction: str):
        """
        Set of instructions on how Plebians move. Plebians
        don't have sophisticated movement, as demonstrated.
        """
        if direction.lower() in self.UP:
            return (self.x, (self.y + 1))
        elif direction.lower() in self.DOWN:
            return (self.x, (self.y - 1))
        elif direction.lower() in self.LEFT:
            return ((self.x - 1), self.y)
        elif direction.lower() in self.RIGHT:
            return ((self.x + 1), self.y)