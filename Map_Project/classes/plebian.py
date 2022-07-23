from classes.abstract.character import Character

class Plebian(Character):
    def __init__(self):
        self.x = None
        self.y = None
        self.position = None
        self.icon = "P"
        self.name = None

    # def set_position(self, x: int, y: int):
    #     self.x = int(x)
    #     self.y = int(y)
    #     self.position = (int(x), int(y))

    # def set_name(self, name: str):
    #     self.name = str(name)

    def movement_action(self, direction: str):
        """
        Set of instructions on how Plebians move. Plebians
        don't have sophisticated movement, as demonstrated.
        """
        if (self.x == None) or (self.y == None):
            raise ValueError("Missing an X or Y (or both, heh) value!")

        if direction.lower() in self.UP:
            return (self.x, (self.y + 1))
        elif direction.lower() in self.DOWN:
            return (self.x, (self.y - 1))
        elif direction.lower() in self.LEFT:
            return ((self.x - 1), self.y)
        elif direction.lower() in self.RIGHT:
            return ((self.x + 1), self.y)
        else:
            print("Error! Direction not recognized. Not moving {}.".format(self.name))
            return (self.x, self.y)