import unittest
from unittest.mock import patch

from classes.game import Game
from classes.plain import Plain
from classes.engines.mapengine import MapEngine
from classes.engines.entityengine import EntityEngine


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
        self.assertNotEqual(crazy_game.map, None)
        self.assertNotEqual(
            crazy_game.map.grid[int(x)][int(y) + 1].occupant,
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
        self.assertNotEqual(super_game.map, None)

    """
    set map tests.
    """
    def test_set_map_success_case(self):
        game_of_tomorrow = Game()
        # New Game should have no map set yet.
        self.assertEqual(game_of_tomorrow.map, None)

        # Note that a Plain IS a map. Specifically, a
        # Plain is a subclass of Map.
        some_plain = Plain()
        game_of_tomorrow.set_map(some_plain)
        self.assertEqual(game_of_tomorrow.map, some_plain)

    def test_set_map_failure_case(self):
        game_of_tomorrow = Game()
        # New Game should have no map set yet.
        self.assertEqual(game_of_tomorrow.map, None)

        # Unfortunately we can't attach sexy beasts to games.
        with self.assertRaises(TypeError) as context:
            game_of_tomorrow.set_map("Hi I'm a sexy beast.")

            self.assertTrue("Unable to attach Map Type obect to Game." in context.exception)

    """
    set map engine tests.
    """
    def test_set_map_engine_success_case(self):
        game_of_tomorrow = Game()
        # New Game should have no map set yet.
        self.assertEqual(game_of_tomorrow.map_engine, None)

        # Note that MapEngine is well, a MapEngine
        engine_of_eternity = MapEngine()
        game_of_tomorrow.set_map_engine(engine_of_eternity)
        self.assertEqual(game_of_tomorrow.map_engine, engine_of_eternity)

    def test_set_map_engine_failure_case(self):
        game_of_tomorrow = Game()
        # New Game should have no map set yet.
        self.assertEqual(game_of_tomorrow.map_engine, None)

        # Insane rabbits in fact, do not count as Map Engines.
        with self.assertRaises(TypeError) as context:
            game_of_tomorrow.set_map_engine("Hello I'm an insane rabbit.")

            self.assertTrue("Unable to attach MapEngine Type obect to Game." in context.exception)

    """
    add character to character list tests.
    """
    @patch('builtins.input', create=True)
    def test_add_character_to_character_list_success_case(self, mocked_input):
        game_of_tomorrow = Game()
        # Create a character. It shouldn't be in the game yet.
        best_entityengine = EntityEngine()
        character_type = "plebian"
        name = "THE DUCK"
        mocked_input.side_effect = [character_type, name]
        duck = best_entityengine.create_character()

        # New Game should have no characters set yet.
        self.assertEqual(game_of_tomorrow.characters, {})

        game_of_tomorrow.add_character_to_character_list(duck)
        self.assertEqual(game_of_tomorrow.characters[name], duck)

    def test_add_character_to_character_list_failure_case(self):
        game_of_tomorrow = Game()
        # New Game should have no characters set yet.
        self.assertEqual(game_of_tomorrow.characters, {})

        # Controverisal opinions can't be added to the character list!
        with self.assertRaises(TypeError) as context:
            game_of_tomorrow.add_character_to_character_list("Controversial Opinions")

            self.assertTrue("Unable to add character type object to the Game's character list." in context.exception)

    @patch('builtins.input', create=True)
    def test_add_character_to_character_list_DUPLICATE_NAME_case(self, mocked_input):
        """
        Try to add a character to the game, but another character with the same name
        already exists in the character list. The new character should not be added
        if there exists a character with the same name.
        """
        game_of_tomorrow = Game()
        best_entityengine = EntityEngine()
        character_type_plebian = "plebian"
        character_type_jester = "jester"
        name = "THE DUCK"
        mocked_input.side_effect = [
            character_type_plebian, name,
            character_type_jester, name
        ]
        duck = best_entityengine.create_character()
        second_duck = best_entityengine.create_character()

        # Assert that the ducks have the same name, but aren't the same entity.
        self.assertEqual(duck.name, second_duck.name)
        self.assertNotEqual(duck, second_duck)

        # New Game should have no characters set yet.
        self.assertEqual(game_of_tomorrow.characters, {})

        # Add the first character no problem.
        game_of_tomorrow.add_character_to_character_list(duck)
        self.assertEqual(game_of_tomorrow.characters[name], duck)

        # Add the "second duck" which shares a name. Shouldn't be added, original
        # index should still be a duck.
        game_of_tomorrow.add_character_to_character_list(second_duck)
        self.assertEqual(game_of_tomorrow.characters[name], duck)
        self.assertNotEqual(game_of_tomorrow.characters[name], second_duck)

    """
    display_game_command tests.
    """
    def test_display_game_commands(self):
        """
        This command is literally just a bunch of print statements, so I'm not quite
        sure how to test this, so I'll just leave it alone for now.
        """
        pass