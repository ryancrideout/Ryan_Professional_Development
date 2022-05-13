from classes.plain import Plain
from classes.jester import Jester
from classes.plebian import Plebian
from classes.abstract.map import Map
from classes.abstract.character import Character


class Game():
    def __init__(self):
        self.map = None

    def set_map(self, map: Map):
        self.map = map

    def run(self):
        """
        Okay we're going to have to figure out how to initialize this whole thing...
        But that's a problem for later?
        """
        # Make a plain. We can implement logic later to choose our map type.
        plain = Plain()
        # Make this a user input
        plain.initialize(10, 10)

        self.set_map(plain)

        # Render the map
        # plain.render()

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
        plain.render()
        print()

        self.move_character(ryan, "Up")
        plain.render()
        print()

        self.move_character(ryan, "R")
        plain.render()
        print()

        self.move_character(ryan, "Left")
        plain.render()
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