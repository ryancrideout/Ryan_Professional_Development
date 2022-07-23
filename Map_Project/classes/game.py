from classes.plain import Plain
from classes.jester import Jester
from classes.plebian import Plebian
from classes.maptile import MapTile
from classes.abstract.map import Map
from classes.abstract.character import Character


class Game():
    TERMINATE = ["stop", "s", "exit", "terminate", "t", "quit", "q"]
    RENDER = ["r", "render", "p", "print"]
    HELP = ["h", "help"]
    CREATE = ["create", "c", "character"]
    MOVE = ["move", "m"]

    def __init__(self):
        self.map = None
        self.characters = {}

    def run(self):
        """
        This runs the game as a whole. There might be an more appropriate place
        for this, but for now I'm putting all of the logic in the "run" method.
        """
        self.initialize_map()

        user_input = input("Now give me a command, type 'help' for a list of available commands - ")
        while user_input.lower() not in self.TERMINATE:

            if user_input.lower() in self.RENDER:
                self.render()

            if user_input.lower() in self.HELP:
                self.display_game_commands()

            if user_input.lower() in self.CREATE:
                character = self.create_character()
                self.set_character_position(character)
                self.add_entity_to_map(character)

            if user_input.lower() in self.MOVE:
                self.move_character()

            user_input = input("Now give me another command - type 'help' for help - ")

        print("Goodbye, human.")

    def set_map(self, map: Map):
        if not isinstance(map, Map):
            raise TypeError("Unable to attach Map Type obect to Game.")
        self.map = map

    def set_maptile_occupant(self, occupant: Character, map_tile: MapTile):
        # RE: Type Checking - while I enforce the occupant to be a character,
        #     I could foresee other "entity" types occupying a map space.
        if occupant == None:
            map_tile.occupant = occupant
        elif not isinstance(occupant, Character):
            raise TypeError("Cannot make a non-character a map occupant!")
        else:
            map_tile.occupant = occupant

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

    def check_if_occupied(self, x_cord: int, y_cord: int) -> bool:
        if self.map == None:
            raise ValueError("There is no map associated with the game!")

        if self.map.grid[x_cord][y_cord].occupant:
            return True
        else:
            return False

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

    def create_character(self):
        """
        Upfront - I'm not super sure how to do this. With this current implementation
                  we'll be violating some SOLID principles.
        """
        # I think we'll need character names and then put that data into a dictionary.
        '''
        # NOTE: If I were running Python 3.10 I could do a switch statement.
                As it stands I run Python 3.9, so I can't do switch statements.
                I could do something like this though if I wanted to:
                https://softwareengineering.stackexchange.com/questions/351389/dynamic-dispatch-from-a-string-python
        '''
        user_input = input("What kind of character do you want to create? ")
        if user_input.lower() == "plebian":
            character = Plebian()
        elif user_input.lower() == "jester":
            character = Jester()
        else:
            print("Unidentified character type. You get a Plebian.")
            character = Plebian()

        name = input("Please give the character a name. - ")
        character.set_name(name)
        self.characters[character.name] = character

        return character

    def set_character_position(self, character):
        # Note that we check for character type, but we might need to expand this later
        # to include more classes. Not 100% sure where I stand on this yet.
        if not isinstance(character, Character):
            raise TypeError("Cannot set position of non-character object!")
        print("Alrigt we need an x and y coordinate to place this character.")
        x_cord = input("X COORDINATE. NOW. - ")
        y_cord = input("NOW A Y COORDINATE - ")
        character.set_position(int(x_cord), int(y_cord))

    def move_character(self):
        # We shouldn't need to do this check, but we have it just in case.
        if self.map == None:
            raise ValueError("There is no map associated with the game!")

        character_name = input("Please give the name of the character you'd like to move - ")
        if character_name not in self.characters:
            raise ValueError("{} is not a character that exists on the map!".format(character_name))
        character = self.characters[character_name]
        direction = input("What direction would you like to move {}? - ".format(character.name))

        desired_position = character.movement_action(direction)
        new_x_cord = desired_position[0]
        new_y_cord = desired_position[1]

        # Out of bounds error checking - if the new_x_cord and new_y_cord are _greater_
        # then the map width and height, then I'll print a message and leave it.
        # I think this is okay, but I have this nagging feeling that this is somehow incorrect...
        if (
            new_x_cord < 0 or
            new_y_cord < 0 or
            new_x_cord > self.map.width or
            new_y_cord > self.map.height
        ):
            print("Cannot move to location! Out of bounds.")
        # Check if desired spot is occupied.
        elif self.check_if_occupied(new_x_cord, new_y_cord):
            print("Cannot move to location! Already occupied.")
        else:
            # Move the character. First, remove character from map.
            self.remove_entity_from_map(character)
            # Set the character's new position
            character.set_position(new_x_cord, new_y_cord)
            # Add the character back to the map.
            self.add_entity_to_map(character)

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

    def display_game_commands(self):
        print("These are the available commands:")
        print()
        print("'terminate' - ends the program.")
        print("'render' - displays the map.")
        print("'help' - displays the game commands.")
        print("'create' - creates a character and puts it on the map.")
        print("'move' - moves a character on a map into a particular direction.")
        print()