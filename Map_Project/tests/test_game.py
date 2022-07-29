import unittest
from unittest.mock import patch

from classes.game import Game


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
    display_game_command tests.
    """
    def test_display_game_commands(self):
        """
        This command is literally just a bunch of print statements, so I'm not quite
        sure how to test this, so I'll just leave it alone for now.
        """
        pass