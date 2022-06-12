from classes.plain import Plain
from classes.jester import Jester
from classes.plebian import Plebian
from classes.abstract.map import Map
from classes.abstract.character import Character


class Game():
    TERMINATE = ["stop", "s", "exit", "terminate", "t"]
    RENDER = ["r", "render", "p", "print"]
    HELP = ["h", "help"]
    CREATE = ["create", "c", "character"]
    MOVE = ["move", "m"]

    def __init__(self):
        self.map = None
        self.characters = {}

    def set_map(self, map: Map):
        if not isinstance(map, Map):
            raise TypeError("Unable to attach Map Type obect to Game.")
        self.map = map

    def run(self):
        """
        This runs the game as a whole. There might be an more appropriate place
        for this, but for now I'm putting all of the logic in the "run" method.
        """
        self.initialize_map()

        user_input = input("Now give me a command, type 'help' for a list of available commands - ")
        while user_input.lower() not in self.TERMINATE:

            if user_input.lower() in self.RENDER:
                self.map.render()

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
            self.map.grid[x_cord][y_cord].set_occupant(entity)
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
            self.map.grid[x_cord][y_cord].set_occupant(None)
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

        name = input("Please give the character a name. - ")
        character.set_name(name)
        self.characters[character.name] = character

        return character

    def set_character_position(self, character):
        # TODO - I need to include error checking.
        print("Alrigt we need an x and y coordinate to place this character.")
        x_cord = input("X COORDINATE. NOW. - ")
        y_cord = input("NOW A Y COORDINATE - ")
        character.set_position(int(x_cord), int(y_cord))

    def move_character(self):
        # TODO - Need to add error checking.
        character_name = input("Please give the name of the character you'd like to move - ")
        character = self.characters[character_name]
        direction = input("What direction would you like to move {}? - ".format(character.name))

        desired_position = character.movement_action(direction)
        new_x_cord = desired_position[0]
        new_y_cord = desired_position[1]

        # Check if desired spot is occupied.
        # TODO: Out of bounds error checking.
        if self.check_if_occupied(new_x_cord, new_y_cord):
            print("Cannot move to location! Already occupied.")
        else:
            # Move the character. First, remove character from map.
            self.remove_entity_from_map(character)
            # Set the character's new position
            character.set_position(new_x_cord, new_y_cord)
            # Add the character back to the map.
            self.add_entity_to_map(character)

    def display_game_commands(self):
        print("These are the available commands:")
        print()
        print("'terminate' - ends the program.")
        print("'render' - displays the map.")
        print("'help' - displays the game commands.")
        print("'create' - creates a character and puts it on the map.")
        print("'move' - moves a character on a map into a particular direction.")
        print()