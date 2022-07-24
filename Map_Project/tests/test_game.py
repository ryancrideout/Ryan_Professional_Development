import unittest
from unittest.mock import patch

from classes.game import Game
from classes.mapengine import MapEngine
from classes.plebian import Plebian
from classes.jester import Jester


class TestGame(unittest.TestCase):
    '''
    NOTE: We're going to have to figure out how to do user inputs for
          unit tests.

          Reference this:
          https://stackoverflow.com/questions/47690020/python-3-unit-tests-with-user-input
    '''
    """
    run tests. "run" as in, the "run" method for the Game Class.
    """
    @patch('builtins.input', create=True)
    def test_run_success_case(self, mocked_input):
        """
        Go through all of the different commands that we have for the "run" method and see that
        they work. We're not going to test the commands too heavily, as that's the point of the
        other unit tests.
        """
        # Values for mocked user inputs.
        map_width = "10"
        map_height = "10"
        render = "render"
        help = "help"
        create = "create"
        character_type = "plebian"
        character_name = "Toucan Sam"
        x = "3"
        y = "3"
        move = "move"
        up = "up"
        terminate = "terminate"

        mocked_input.side_effect = [
            map_width,
            map_height,
            # Render command
            render,
            # Help Command
            help,
            # Create Character Command
            create,
            character_type,
            character_name,
            x,
            y,
            # Move Character Command
            move,
            character_name,
            up,
            # Terminate Command
            terminate,
        ]

        crazy_game = Game()
        crazy_game.run()

        # After all of that tom-foolery we should have a map attached to the game.
        self.assertNotEqual(crazy_game.map_engine.map, None)
        self.assertNotEqual(
            crazy_game.map_engine.map.grid[int(x)][int(y) + 1].occupant,
            None
        )

    @patch('builtins.input', create=True)
    def test_run_unrecognized_input_case(self, mocked_input):
        """
        The test case where we try to feed the interpreter some unrecognized inputs.
        Nothing should happen, but we should be able to terminate if we want to.
        """
        # Values for mocked user inputs.
        map_width = "10"
        map_height = "10"
        unrecognized_input = "And the flames will rise!"
        terminate = "terminate"

        mocked_input.side_effect = [
            map_width,
            map_height,
            unrecognized_input,
            terminate
        ]

        super_game = Game()
        super_game.run()

        # The game should run (and close), and with this pass we should only have the
        # map set for game, so it should NOT be "None".
        self.assertNotEqual(super_game.map_engine.map, None)

    """
    create_character tests.
    """
    @patch('classes.game.input', create=True)
    def test_create_character_plebian_case(self, mocked_input):
        """
        Create ourselves a plebian. We'll be sure to give them a great name.
        """
        best_game = Game()
        character_type = "plebian"
        name = "The Fresh Kid"
        mocked_input.side_effect = [character_type, name]

        # Create our character and assert that the class and name is right.
        fresh_meat = best_game.create_character()
        self.assertTrue(isinstance(fresh_meat, Plebian))
        self.assertEqual(fresh_meat.name, name)

    @patch('classes.game.input', create=True)
    def test_create_character_jester_case(self, mocked_input):
        """
        Almost identical to the first test, though in this case we're making a jester.
        """
        best_game = Game()
        character_type = "JeStEr"
        name = "King Snuffles"
        mocked_input.side_effect = [character_type, name]

        # Create our character and assert that the class and name is right.
        not_plebian = best_game.create_character()
        self.assertTrue(isinstance(not_plebian, Jester))
        self.assertEqual(not_plebian.name, name)

    @patch('classes.game.input', create=True)
    def test_create_character_unspecified_case(self, mocked_input):
        """
        The case where we give a character type that's undefined or not known.
        This will give us back a Plebian.
        """
        best_game = Game()
        character_type = "Epic Tier 3 Engineer"
        name = "Isaac Clarke"
        mocked_input.side_effect = [character_type, name]

        # Create our character and assert that the class and name is right.
        engineer = best_game.create_character()
        self.assertTrue(isinstance(engineer, Plebian))
        self.assertEqual(engineer.name, name)

    """
    set_character_position tests.
    """
    @patch('classes.game.input', create=True)
    def test_set_character_position_success_case(self, mocked_input):
        """
        Have a character, and set it's position. Pretty straightforward. I hope.

        Note that the inputs get cast to int, hence the string and int input.

        Also note that setting the character position is independent of the map so
        trying to set a character's position to be outside of map bounds is futile.
        """
        power_game = Game()
        the_coach = Plebian()
        x_cord = "2"
        y_cord = 2
        mocked_input.side_effect = [x_cord, y_cord]

        # Nothing should be set yet.
        self.assertEqual(the_coach.position, None)
        self.assertEqual(the_coach.x, None)
        self.assertEqual(the_coach.y, None)

        power_game.set_character_position(the_coach)

        self.assertEqual(the_coach.position, (int(x_cord), y_cord))
        self.assertEqual(the_coach.x, int(x_cord))
        self.assertEqual(the_coach.y, y_cord)

    def test_set_character_position_NON_CHARACTER_case(self):
        """
        Case where we try to set the character position of a non character.

        This should end in heartbreak and failure.
        """
        power_game = Game()
        with self.assertRaises(TypeError) as context:
            power_game.set_character_position("Big Chungus lives on as the dominant meme")

            self.assertTrue("Cannot set position of non-character object!" in context.exception)

    @patch('classes.game.input', create=True)
    def test_set_character_position_dumb_input_case(self, mocked_input):
        """
        Case where we try some outrageously stupid inputs for the method. Ideally, things should break.
        """
        power_game = Game()
        harvey_dent = Jester()
        x_cord = "War. War never changes."
        y_cord = Game()
        mocked_input.side_effect = [x_cord, y_cord]

        with self.assertRaises(ValueError):
            power_game.set_character_position(harvey_dent)

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
        chump_game.set_map_engine(the_mapengine)
        the_mapengine.initialize_map()
        plebian_isaac = chump_game.create_character()
        chump_game.set_character_position(plebian_isaac)
        the_mapengine.add_entity_to_map(plebian_isaac)

        # Make sure Isaac is on the map.
        self.assertEqual(
            the_mapengine.map.grid[int(char_starting_x)][int(char_starting_y)].occupant,
            plebian_isaac
        )

        # Move Isaac "Up"
        chump_game.move_character()
        self.assertEqual(
            the_mapengine.map.grid[int(char_starting_x)][int(char_starting_y) + 1].occupant,
            plebian_isaac
        )

        # Move Isaac "Down"
        chump_game.move_character()
        self.assertEqual(
            the_mapengine.map.grid[int(char_starting_x)][int(char_starting_y)].occupant,
            plebian_isaac
        )

        # Move Isaac "Left"
        chump_game.move_character()
        self.assertEqual(
            the_mapengine.map.grid[int(char_starting_x) - 1][int(char_starting_y)].occupant,
            plebian_isaac
        )

        # Move Isaac "Right"
        chump_game.move_character()
        self.assertEqual(
            the_mapengine.map.grid[int(char_starting_x)][int(char_starting_y)].occupant,
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
        chump_game.set_map_engine(the_mapengine)
        the_mapengine.initialize_map()

        with self.assertRaises(ValueError) as context:
            chump_game.move_character()

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
        chump_game.set_map_engine(the_mapengine)
        the_mapengine.initialize_map()

        # Add Isaac to the map and make sure he's there.
        plebian_isaac = chump_game.create_character()
        chump_game.set_character_position(plebian_isaac)
        the_mapengine.add_entity_to_map(plebian_isaac)
        self.assertEqual(
            the_mapengine.map.grid[int(char_1_starting_x)][int(char_1_starting_y)].occupant,
            plebian_isaac
        )

        # Add Darius to the map and make sure he's there.
        jester_darius = chump_game.create_character()
        chump_game.set_character_position(jester_darius)
        the_mapengine.add_entity_to_map(jester_darius)
        self.assertEqual(
            the_mapengine.map.grid[int(char_2_starting_x)][int(char_2_starting_y)].occupant,
            jester_darius
        )

        # Attempt to move Isaac up. This shouldn't fly as Darius is already in that spot.
        # As such Isaac should still be in the same spot. Same as Darius, for that matter.
        chump_game.move_character()
        self.assertEqual(
            the_mapengine.map.grid[int(char_1_starting_x)][int(char_1_starting_y)].occupant,
            plebian_isaac
        )
        self.assertEqual(
            the_mapengine.map.grid[int(char_2_starting_x)][int(char_2_starting_y)].occupant,
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
        chump_game.set_map_engine(the_mapengine)
        plebian_isaac = chump_game.create_character()
        chump_game.set_character_position(plebian_isaac)
        # Normally the error would occur here, but that's not what we're trying to test.
        # chump_game.add_entity_to_map(plebian_isaac)

        with self.assertRaises(ValueError) as context:
            chump_game.move_character()

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
        chump_game.set_map_engine(the_mapengine)
        the_mapengine.initialize_map()
        plebian_isaac = chump_game.create_character()
        chump_game.set_character_position(plebian_isaac)
        the_mapengine.add_entity_to_map(plebian_isaac)

        # Make sure Isaac is on the map.
        self.assertEqual(
            the_mapengine.map.grid[int(char_starting_x)][int(char_starting_y)].occupant,
            plebian_isaac
        )

        # Try to move Isaac "Down". He shouldn't end up moving anywhere so his position
        # should stay the same.
        chump_game.move_character()
        self.assertEqual(
            the_mapengine.map.grid[int(char_starting_x)][int(char_starting_y)].occupant,
            plebian_isaac
        )

    """
    set_entity_position tests
    """
    def test_set_entity_position_success_case(self):
        """
        Set the position for both the Jester and Plebian. Functionality
        will be the same for both classes.
        """
        hugh_jackman = Plebian()
        jugh_hackman = Jester()
        chump_game = Game()

        x_cord = 14
        y_cord = 16

        # No position should be set yet for either character.
        self.assertEqual(hugh_jackman.x, None)
        self.assertEqual(hugh_jackman.y, None)
        self.assertEqual(hugh_jackman.position, None)
        # This is "Jugh", not "Hugh".
        # Note I deliberately swapped the X and Y coordinates.
        self.assertEqual(jugh_hackman.x, None)
        self.assertEqual(jugh_hackman.y, None)
        self.assertEqual(jugh_hackman.position, None)

        # SET SOME POSITIONS
        chump_game.set_entity_position(hugh_jackman, x_cord, y_cord)
        chump_game.set_entity_position(jugh_hackman, y_cord, x_cord)

        self.assertEqual(hugh_jackman.x, x_cord)
        self.assertEqual(hugh_jackman.y, y_cord)
        self.assertEqual(hugh_jackman.position, (x_cord, y_cord))
        # Remember, this is "Jugh" time. 
        self.assertEqual(jugh_hackman.x, y_cord)
        self.assertEqual(jugh_hackman.y, x_cord)
        self.assertEqual(jugh_hackman.position, (y_cord, x_cord))

    def test_set_entity_position_CAST_TO_INT_case(self):
        """
        Set the position for both the Jester and Plebian. Functionality
        will be the same for both classes.
        """
        captain_commando = Plebian()
        jin = Jester()
        chump_game = Game()

        x_cord = "21"
        y_cord = "18"

        # SET SOME POSITIONS
        chump_game.set_entity_position(captain_commando, x_cord, y_cord)
        chump_game.set_entity_position(jin, y_cord, x_cord)

        self.assertEqual(captain_commando.x, int(x_cord))
        self.assertEqual(captain_commando.y, int(y_cord))
        self.assertEqual(captain_commando.position, (int(x_cord), int(y_cord)))
        # BLOODIA!
        self.assertEqual(jin.x, int(y_cord))
        self.assertEqual(jin.y, int(x_cord))
        self.assertEqual(jin.position, (int(y_cord), int(x_cord)))

    def test_set_entity_position_FAILURE_case(self):
        """
        Testing the set_entity_position command with inputs that should cause it to EXPLODE.
        This is just to ensure that the type checking remains intact.
        """
        hogwash = Plebian()
        bustah_wolf = Jester()
        chump_game = Game()

        x_cord = "Do dogs like to backflip?"
        y_cord = bustah_wolf

        with self.assertRaises(ValueError) as context:
            chump_game.set_entity_position(hogwash, x_cord, y_cord)

        with self.assertRaises(TypeError) as context:
            chump_game.set_entity_position(hogwash, y_cord, x_cord)

    """
    set_entity_name tests
    """
    def test_set_entity_name_success_case(self):
        """
        Default set name case. Due to type checking, "ints" are acceptable inputs.
        """
        some_guy = Plebian()
        some_gal = Jester()
        chump_game = Game()

        name_one = "Bruce, the Strongest One"
        name_two = 12003100

        # No names should be set yet.
        self.assertEqual(some_guy.name, None)
        self.assertEqual(some_gal.name, None)

        chump_game.set_entity_name(some_guy, name_one)
        chump_game.set_entity_name(some_gal, name_two)

        self.assertEqual(some_guy.name, name_one)
        self.assertEqual(some_gal.name, str(name_two))

    """
    display_game_command tests.
    """
    def test_display_game_commands(self):
        """
        This command is literally just a bunch of print statements, so I'm not quite
        sure how to test this, so I'll just leave it alone for now.
        """
        pass