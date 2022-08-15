from classes.abstract.map import Map
from classes.abstract.character import Character

from classes.engines.mapengine import MapEngine
from classes.engines.entityengine import EntityEngine
from classes.engines.movementengine import MovementEngine


class Game():
    TERMINATE = ["stop", "s", "exit", "terminate", "t", "quit", "q"]
    RENDER = ["r", "render", "p", "print"]
    HELP = ["h", "help"]
    CREATE = ["create", "c", "character"]
    MOVE = ["move", "m"]

    def __init__(self):
        self.map = None
        self.characters = {}

        # Engines to help run the game.
        self.map_engine = None
        self.entity_engine = None
        self.movement_engine = None

    def set_map_engine(self, map_engine):
        """
        Helper function to help with unit tests.
        """
        self.map_engine = map_engine

    def set_up(self):
        # Function to set up all of our variables. For now, this might not be necessary,
        # but as codebase expands this could be good to have.
        self.map_engine = MapEngine()
        self.entity_engine = EntityEngine()
        self.movement_engine = MovementEngine()

    def set_map(self, map: Map):
        if not isinstance(map, Map):
            raise TypeError("Unable to attach Map Type obect to Game.")
        self.map = map

    def add_character_to_character_list(self, character: Character):
        if not isinstance(character, Character):
            raise TypeError("Unable to add character type object to the Game's character list.")
        self.characters[character.name] = character

    def run(self):
        """
        This runs the game as a whole. There might be an more appropriate place
        for this, but for now I'm putting all of the logic in the "run" method.
        """
        self.set_up()
        self.map = self.map_engine.initialize_map()

        user_input = input("Now give me a command, type 'help' for a list of available commands - ")
        while user_input.lower() not in self.TERMINATE:

            if user_input.lower() in self.RENDER:
                self.map_engine.render(self.map)

            if user_input.lower() in self.HELP:
                self.display_game_commands()

            if user_input.lower() in self.CREATE:
                character = self.entity_engine.create_character()
                # TODO: Add error checking so we don't 'overwrite' characters
                self.add_character_to_character_list(character)
                self.entity_engine.set_character_position(character)
                self.map_engine.add_entity_to_map(self.map, character)

            if user_input.lower() in self.MOVE:
                self.movement_engine.move_entity(
                    self.map, 
                    self.characters,
                    self.map_engine,
                    self.entity_engine,
                )

            user_input = input("Now give me another command - type 'help' for help - ")

        print("Goodbye, human.")

    def display_game_commands(self):
        print("These are the available commands:")
        print()
        print("'terminate' - ends the program.")
        print("'render' - displays the map.")
        print("'help' - displays the game commands.")
        print("'create' - creates a character and puts it on the map.")
        print("'move' - moves a character on a map into a particular direction.")
        print()