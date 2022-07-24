from classes.plain import Plain
from classes.maptile import MapTile
from classes.abstract.map import Map
from classes.abstract.character import Character

class MapEngine():
    """
    This is a class that handles all of the map related tasks.

    To be operated by the game class.
    """
    def __init__(self):
        self.map = None

    def initialize_map(self):
        """
        TODO - I could flesh this out with more robust checks, but
               for now I'm not going to. I know how to, but I won't
               touch it until the need arises.
        """
        print("We're going to make a map. We're going to need width and height.")
        width = input("Hey give me an width you... you... FIEND - ")
        height = input("AND NOW GIVE ME A HEIGHT - ")
        print("Here are the coordinates you gave - ({}, {})".format(width, height))
        print()

        # Make a plain. We can implement logic later to choose our map type.
        plain = Plain()
        plain.initialize(int(width), int(height))

        self.set_map(plain)

    def set_map(self, map: Map):
        if not isinstance(map, Map):
            raise TypeError("Unable to attach Map Type obect to Game.")
        self.map = map

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
        if not self.map:
            print("There is no map you display! AUGH!")
        elif not self.map.grid:
            print("Map has no grid attached to it!")
        else:
            # TODO: Verify I got the width and height correct.
            #       I have my doubts.
            for i in range(self.map.height):
                y_index = self.map.height - 1 - i
                print(f"\n", end="")
                for x_index in range(self.map.width):
                    if self.map.grid[x_index][y_index].occupant:
                        print("|{}".format(self.map.grid[x_index][y_index].occupant.icon), end="")
                    else:
                        print("| ", end="")
                print("|", end="")
        print()

    def add_entity_to_map(self, entity):
        """
        This takes an entity (E.G., Character) and adds it to the map.

        Note the entity doesn't HAVE to be a character, which is why I didn't
        enforce type checking. I'm just thinking in the future if... say...
        we added non-character entities like a treasure chest or something.
        """
        if self.map == None:
            raise ValueError("There is no map associated with the game!")

        x_cord = entity.x
        y_cord = entity.y

        # Need to do - add error checking.
        if not self.map.grid[x_cord][y_cord].occupant:
            self.set_maptile_occupant(entity, self.map.grid[x_cord][y_cord])
        else:
            # AttributeError might not be the appropriate error to raise here?
            raise AttributeError("Map space is already occupied!")

    def remove_entity_from_map(self, entity):
        """
        We're making an assumption with this method that the entity already
        exists on the map.
        """
        if self.map == None:
            raise ValueError("There is no map associated with the game!")

        x_cord = entity.x
        y_cord = entity.y

        # Again, need to add some error checking or something.
        if self.map.grid[x_cord][y_cord].occupant:
            self.set_maptile_occupant(None, self.map.grid[x_cord][y_cord])
        else:
            # We might need a better error message here.
            print("{}, {} is already empty!".format(x_cord, y_cord))

    def set_maptile_occupant(self, occupant: Character, map_tile: MapTile):
        # RE: Type Checking - while I enforce the occupant to be a character,
        #     I could foresee other "entity" types occupying a map space.
        if occupant == None:
            map_tile.occupant = occupant
        elif not isinstance(occupant, Character):
            raise TypeError("Cannot make a non-character a map occupant!")
        else:
            map_tile.occupant = occupant

    def check_if_occupied(self, x_cord: int, y_cord: int) -> bool:
        if self.map == None:
            raise ValueError("There is no map associated with the game!")

        if self.map.grid[x_cord][y_cord].occupant:
            return True
        else:
            return False
