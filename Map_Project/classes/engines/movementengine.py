class MovementEngine():

    def move_entity(self):
        # Okay so... what do we need here?
        # - Character
        # - New X & Y Coordinates
        # - Map
        #    - Whether or not the space is occupied

        # Then the question has to be, how do we get all of that information?

        # I think maybe we put the variables back into the Game Class? Then we can pass them around.

        # WHAT NOT TO DO:
        # Pass in the entire engine, all of the variables we need aren't necessarily an engine.

        # Possibly we take the whole method and put in here? 

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
            map_engine.add_entity_to_map(character)
        """