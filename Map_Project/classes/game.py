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

    def set_map(self, map: Map):
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
                print("Quoi")
            if user_input.lower() in self.MOVE:
                print("Shoryuken")
            input("Now give me another command - type 'help' for help")

        print("Goodbye, human.")

        leonidas = Plebian()
        # Set coordinates, but make this a user input.
        leonidas.set_position(3, 3)
        self.add_entity_to_map(leonidas)
        # plain.render()
        # print()

        self.move_character(leonidas, "South")
        # plain.render()
        # print()

        ryan = Jester()
        ryan.set_position(5, 5)
        self.add_entity_to_map(ryan)
        self.map.render()
        print()

        self.move_character(ryan, "Up")
        self.map.render()
        print()

        self.move_character(ryan, "R")
        self.map.render()
        print()

        self.move_character(ryan, "Left")
        self.map.render()
        print()

        # TODO: Flesh this out some more, actually make this a "game",
        #       ask user for prompts and then add characters and then
        #       make them move.

    def move_character(self, character: Character, direction: str):
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

    def add_entity_to_map(self, entity):
        """
        This takes an entity (E.G., Character) and adds it to the map.
        """
        x_cord = entity.x
        y_cord = entity.y

        # Need to do - add error checking.
        if not self.map.grid[x_cord][y_cord].occupant:
            self.map.grid[x_cord][y_cord].set_occupant(entity)

    def remove_entity_from_map(self, entity):
        """
        We're making an assumption with this method that the entity already
        exists on the map.
        """
        x_cord = entity.x
        y_cord = entity.y

        # Again, need to add some error checking or something.
        if self.map.grid[x_cord][y_cord].occupant:
            self.map.grid[x_cord][y_cord].set_occupant(None)

    def check_if_occupied(self, x_cord: int, y_cord: int) -> bool:
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
        width = input("Hey give me an width you... you... FIEND - ")
        height = input("AND NOW GIVE ME A HEIGHT - ")
        print("Here are the coordinates you gave - ({}, {})".format(width, height))

        # Make a plain. We can implement logic later to choose our map type.
        plain = Plain()
        plain.initialize(int(width), int(height))

        self.set_map(plain)

    def create_character(self):
        """
        Upfront - I did this in a really bad and lazy way because I just ran
        out of steam. The big TO do is to go clean this up later.
        """
        # I think we'll need character names and then put that data into a dictionary.
        print("Shoryuken.")

    def move_character(self):
        print("Shoryuken.")

    def display_game_commands(self):
        print("These are the available commands:")
        print()
        print("'terminate' - ends the program.")
        print("'render' - displays the map.")
        print("'help' - displays the game commands.")
        print("'create' - creates a character and puts it on the map.")
        print("'move' - moves a character on a map into a particular direction.")
        print()