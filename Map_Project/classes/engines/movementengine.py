from classes.abstract.map import Map
from classes.engines.mapengine import MapEngine
from classes.engines.entityengine import EntityEngine


class MovementEngine():
    """
    I thought about having the MovementEngine inherit from multiple engines, but that seems... wrong?
    Like it seems like we're introducing more variables when maybe we don't need to.

    Also, then, the problem is what happens when we need multiple engines?
    """
    def move_entity(
        self, 
        map: Map, 
        characters: dict,
        mapengine: MapEngine,
        entityengine: EntityEngine,
        ):

        character_name = input("Please give the name of the character you'd like to move - ")
        if character_name not in characters:
            raise ValueError("{} is not a character that exists on the map!".format(character_name))
        character = characters[character_name]
        direction = input("What direction would you like to move {}? - ".format(character.name))

        desired_position = character.movement_action(direction)
        new_x_cord = desired_position[0]
        new_y_cord = desired_position[1]

        # We shouldn't need to do this check, but we have it just in case.
        if map == None:
            raise ValueError("There is no map associated with the game!")

        # Out of bounds error checking - if the new_x_cord and new_y_cord are _greater_
        # then the map width and height, then I'll print a message and leave it.
        # I think this is okay, but I have this nagging feeling that this is somehow incorrect...
        if (
            new_x_cord < 0 or
            new_y_cord < 0 or
            new_x_cord > map.width or
            new_y_cord > map.height
        ):
            print("Cannot move to location! Out of bounds.")
        # Check if desired spot is occupied.
        elif mapengine.check_if_occupied(map, new_x_cord, new_y_cord):
            print("Cannot move to location! Already occupied.")
        else:
            # Move the character. First, remove character from map.
            mapengine.remove_entity_from_map(map, character)
            # Set the character's new position
            entityengine.set_entity_position(character, new_x_cord, new_y_cord)
            # Add the character back to the map.
            mapengine.add_entity_to_map(map, character)
