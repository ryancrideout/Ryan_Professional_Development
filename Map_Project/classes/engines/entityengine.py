from classes.jester import Jester
from classes.plebian import Plebian
from classes.abstract.character import Character


class EntityEngine():
    """
    This is a class that handles all of the entity (e.g., character) related tasks.

    To be operated by the game class.
    """
    def create_character(self):
        """
        Upfront - I'm not super sure how to do this. With this current implementation
                  we'll be violating some SOLID principles.
        """
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

        return character

    def set_character_position(self, character: Character):
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
