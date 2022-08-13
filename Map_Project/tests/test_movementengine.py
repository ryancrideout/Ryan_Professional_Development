import unittest
from unittest.mock import patch

from classes.game import Game
from classes.engines.mapengine import MapEngine
from classes.engines.entityengine import EntityEngine
from classes.engines.movementengine import MovementEngine


class TestMovementEngine(unittest.TestCase):
    """
    move_character tests.
    """
    @patch('builtins.input', create=True)
    def test_move_character_success_case(self, mocked_input):
        """
        Simple test to see if we can move a character on the map. Note that the movement
        actions are tied to the character classes themselves, so we'll test those more
        rigorously for those tests.
        """
        # Values for mocked user inputs.
        map_width = "10"
        map_height = "10"
        character_type = "plebian"
        character_name = "Isaac"
        char_starting_x = "3"
        char_starting_y = "3"
        up = "up"
        down = "down"
        left = "left"
        right = "right"

        mocked_input.side_effect = [
            map_width,
            map_height,
            character_type,
            character_name,
            char_starting_x,
            char_starting_y,
            # Need character name to specify who to move
            character_name,
            up,
            character_name,
            down,
            character_name,
            left,
            character_name,
            right,
        ]

        # Set up to put the character on the map
        chump_game = Game()
        the_mapengine = MapEngine()
        the_entityengine = EntityEngine()
        # chump_game.set_map_engine(the_mapengine)
        thug_map = the_mapengine.initialize_map()
        chump_game.set_map(thug_map)
        plebian_isaac = the_entityengine.create_character()
        the_entityengine.set_character_position(plebian_isaac)
        the_mapengine.add_entity_to_map(thug_map, plebian_isaac)
        chump_game.add_character_to_character_list(plebian_isaac)

        # Make sure Isaac is on the map.
        self.assertEqual(
            chump_game.map.grid[int(char_starting_x)][int(char_starting_y)].occupant,
            plebian_isaac
        )

        # Move Isaac "Up"
        the_entityengine.move_character(
            chump_game.map,
            chump_game.characters,
            the_mapengine,
            the_entityengine,
        )
        self.assertEqual(
            chump_game.map.grid[int(char_starting_x)][int(char_starting_y) + 1].occupant,
            plebian_isaac
        )

        # Move Isaac "Down"
        the_entityengine.move_character(
            chump_game.map,
            chump_game.characters,
            the_mapengine,
            the_entityengine,
        )
        self.assertEqual(
            chump_game.map.grid[int(char_starting_x)][int(char_starting_y)].occupant,
            plebian_isaac
        )

        # Move Isaac "Left"
        the_entityengine.move_character(
            chump_game.map,
            chump_game.characters,
            the_mapengine,
            the_entityengine,
        )
        self.assertEqual(
            chump_game.map.grid[int(char_starting_x) - 1][int(char_starting_y)].occupant,
            plebian_isaac
        )

        # Move Isaac "Right"
        the_entityengine.move_character(
            chump_game.map,
            chump_game.characters,
            the_mapengine,
            the_entityengine,
        )
        self.assertEqual(
            chump_game.map.grid[int(char_starting_x)][int(char_starting_y)].occupant,
            plebian_isaac
        )

    @patch('builtins.input', create=True)
    def test_move_character_non_existent_character_case(self, mocked_input):
        """
        Try to move a character who just doesn't exist. Big sad.
        """
        # Values for mocked user inputs.
        map_width = "10"
        map_height = "10"
        character_name = "King Darius"

        mocked_input.side_effect = [
            map_width,
            map_height,
            character_name,
        ]

        chump_game = Game()
        the_mapengine = MapEngine()
        the_entityengine = EntityEngine()
        # chump_game.set_map_engine(the_mapengine)
        thug_map = the_mapengine.initialize_map()
        chump_game.set_map(thug_map)

        with self.assertRaises(ValueError) as context:
            the_entityengine.move_character(
                chump_game.map,
                chump_game.characters,
                the_mapengine,
                the_entityengine,
            )

            self.assertTrue("{} is not a character that exists on the map!".format(character_name) in context.exception)

    @patch('builtins.input', create=True)
    def test_move_character_already_occupied_case(self, mocked_input):
        """
        Now we try to move a chracter to a spot that is already occupied.

        Obviously we can't move them to that position, just like in real life.
        """
        # Values for mocked user inputs.
        map_width = "10"
        map_height = "10"
        character_1_type = "plebian"
        character_1_name = "Isaac"
        char_1_starting_x = "3"
        char_1_starting_y = "3"
        character_2_type = "jester"
        character_2_name = "Darius"
        char_2_starting_x = "3"
        char_2_starting_y = "4"
        up = "up"
        mocked_input.side_effect = [
            map_width,
            map_height,
            character_1_type,
            character_1_name,
            char_1_starting_x,
            char_1_starting_y,
            character_2_type,
            character_2_name,
            char_2_starting_x,
            char_2_starting_y,
            # Need character name to specify who to move
            character_1_name,
            up,
        ]

        # Set up to put the character on the map
        chump_game = Game()
        the_mapengine = MapEngine()
        the_entityengine = EntityEngine()
        # chump_game.set_map_engine(the_mapengine)
        thug_map = the_mapengine.initialize_map()
        chump_game.set_map(thug_map)

        # Add Isaac to the map and make sure he's there.
        plebian_isaac = the_entityengine.create_character()
        chump_game.add_character_to_character_list(plebian_isaac)
        the_entityengine.set_character_position(plebian_isaac)
        the_mapengine.add_entity_to_map(thug_map, plebian_isaac)
        self.assertEqual(
            chump_game.map.grid[int(char_1_starting_x)][int(char_1_starting_y)].occupant,
            plebian_isaac
        )

        # Add Darius to the map and make sure he's there.
        jester_darius = the_entityengine.create_character()
        chump_game.add_character_to_character_list(jester_darius)
        the_entityengine.set_character_position(jester_darius)
        the_mapengine.add_entity_to_map(thug_map, jester_darius)
        self.assertEqual(
            chump_game.map.grid[int(char_2_starting_x)][int(char_2_starting_y)].occupant,
            jester_darius
        )

        # Attempt to move Isaac up. This shouldn't fly as Darius is already in that spot.
        # As such Isaac should still be in the same spot. Same as Darius, for that matter.
        the_entityengine.move_character(
            chump_game.map,
            chump_game.characters,
            the_mapengine,
            the_entityengine,
        )
        self.assertEqual(
            chump_game.map.grid[int(char_1_starting_x)][int(char_1_starting_y)].occupant,
            plebian_isaac
        )
        self.assertEqual(
            chump_game.map.grid[int(char_2_starting_x)][int(char_2_starting_y)].occupant,
            jester_darius
        )

    @patch('builtins.input', create=True)
    def test_move_character_NO_MAP_case(self, mocked_input):
        """
        Try to move a character when we have no map attached to the game. As expected this
        should fail. If not, go order a pizza or something. Maybe? I don't know.
        """
        # Values for mocked user inputs.
        character_type = "plebian"
        character_name = "Isaac"
        char_starting_x = "3"
        char_starting_y = "3"
        up = "up"
        mocked_input.side_effect = [
            character_type,
            character_name,
            char_starting_x,
            char_starting_y,
            # Need character name to specify who to move
            character_name,
            up,
        ]

        # Set up to put the character on the map
        chump_game = Game()
        the_mapengine = MapEngine()
        the_entityengine = EntityEngine()
        # chump_game.set_map_engine(the_mapengine)
        plebian_isaac = the_entityengine.create_character()
        chump_game.add_character_to_character_list(plebian_isaac)
        the_entityengine.set_character_position(plebian_isaac)
        # Normally the error would occur here, but that's not what we're trying to test.
        # chump_game.add_entity_to_map(plebian_isaac)

        with self.assertRaises(ValueError) as context:
            the_entityengine.move_character(
                chump_game.map,
                chump_game.characters,
                the_mapengine,
                the_entityengine,
            )

            self.assertTrue("There is no map associated with the game!" in context.exception)

    @patch('builtins.input', create=True)
    def test_move_character_OUT_OF_BOUNDS_case(self, mocked_input):
        """
        Try to move a character out of bounds - a message should be printed (though we won't see it),
        but we won't end up moving the character at all.
        """
        # Values for mocked user inputs.
        map_width = "10"
        map_height = "10"
        character_type = "plebian"
        character_name = "Isaac"
        char_starting_x = "0"
        char_starting_y = "0"
        down = "down"
        mocked_input.side_effect = [
            map_width,
            map_height,
            character_type,
            character_name,
            char_starting_x,
            char_starting_y,
            # Need character name to specify who to move
            character_name,
            down,
        ]

        # Set up to put the character on the map
        chump_game = Game()
        the_mapengine = MapEngine()
        the_entityengine = EntityEngine()
        # chump_game.set_map_engine(the_mapengine)
        thug_map = the_mapengine.initialize_map()
        chump_game.set_map(thug_map)
        plebian_isaac = the_entityengine.create_character()
        chump_game.add_character_to_character_list(plebian_isaac)
        the_entityengine.set_character_position(plebian_isaac)
        the_mapengine.add_entity_to_map(thug_map, plebian_isaac)

        # Make sure Isaac is on the map.
        self.assertEqual(
            chump_game.map.grid[int(char_starting_x)][int(char_starting_y)].occupant,
            plebian_isaac
        )

        # Try to move Isaac "Down". He shouldn't end up moving anywhere so his position
        # should stay the same.
        the_entityengine.move_character(
            chump_game.map,
            chump_game.characters,
            the_mapengine,
            the_entityengine,
        )
        self.assertEqual(
            chump_game.map.grid[int(char_starting_x)][int(char_starting_y)].occupant,
            plebian_isaac
        )