from classes.jester import Jester
from classes.plebian import Plebian
from classes.abstract.character import Character


class EntityEngine():
    """
    This is a class that handles all of the entity (e.g., character) related tasks.

    To be operated by the game class.
    """
    def __init__(self):
        self.characters = {}

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
        self.set_entity_name(character, name)
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
        self.set_entity_position(character, int(x_cord), int(y_cord))

    def set_entity_position(self, entity, x: int, y: int):
        """
        Not sure how I feel about this particular function because I feel like
        it's very close to doing what "set_character_position" is doing, but
        is actually setting the position. I guess this is a helper function
        more than anything.
        """
        entity.x = int(x)
        entity.y = int(y)
        entity.position = (int(x), int(y))

    def set_entity_name(self, entity, name):
        entity.name = str(name)

    # Be sure to remove the map_engine
    def move_character(self, map_engine):
        """
        Not sure if this method should live in the Map Engine or the Character Engine,
        so for now it'll just live in the Game class.
        """
        character_name = input("Please give the name of the character you'd like to move - ")
        if character_name not in self.characters:
            raise ValueError("{} is not a character that exists on the map!".format(character_name))
        character = self.characters[character_name]
        direction = input("What direction would you like to move {}? - ".format(character.name))

        desired_position = character.movement_action(direction)
        new_x_cord = desired_position[0]
        new_y_cord = desired_position[1]

        # We shouldn't need to do this check, but we have it just in case.
        if map_engine.map == None:
            raise ValueError("There is no map associated with the game!")

        # Out of bounds error checking - if the new_x_cord and new_y_cord are _greater_
        # then the map width and height, then I'll print a message and leave it.
        # I think this is okay, but I have this nagging feeling that this is somehow incorrect...
        if (
            new_x_cord < 0 or
            new_y_cord < 0 or
            new_x_cord > map_engine.map.width or
            new_y_cord > map_engine.map.height
        ):
            print("Cannot move to location! Out of bounds.")
        # Check if desired spot is occupied.
        elif map_engine.check_if_occupied(new_x_cord, new_y_cord):
            print("Cannot move to location! Already occupied.")
        else:
            # Move the character. First, remove character from map.
            map_engine.remove_entity_from_map(character)
            # Set the character's new position
            self.set_entity_position(character, new_x_cord, new_y_cord)
            # Add the character back to the map.
            map_engine.add_entity_to_map(map_engine.map, character)