import unittest

from classes.plebian import Plebian
from classes.jester import Jester

"""
Note that here we're just testing the character classes in general here -
I don't think there's enough difference between the character classes to 
warrant separate test files.
"""
class TestCharacters(unittest.TestCase):
    """
    set_position tests
    """
    def test_set_position_success_case(self):
        """
        Set the position for both the Jester and Plebian. Functionality
        will be the same for both classes.
        """
        hugh_jackman = Plebian()
        jugh_hackman = Jester()

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
        hugh_jackman.set_position(x_cord, y_cord)
        jugh_hackman.set_position(y_cord, x_cord)

        self.assertEqual(hugh_jackman.x, x_cord)
        self.assertEqual(hugh_jackman.y, y_cord)
        self.assertEqual(hugh_jackman.position, (x_cord, y_cord))
        # Remember, this is "Jugh" time. 
        self.assertEqual(jugh_hackman.x, y_cord)
        self.assertEqual(jugh_hackman.y, x_cord)
        self.assertEqual(jugh_hackman.position, (y_cord, x_cord))

    def test_set_position_CAST_TO_INT_case(self):
        """
        Set the position for both the Jester and Plebian. Functionality
        will be the same for both classes.
        """
        captain_commando = Plebian()
        jin = Jester()

        x_cord = "21"
        y_cord = "18"

        # SET SOME POSITIONS
        captain_commando.set_position(x_cord, y_cord)
        jin.set_position(y_cord, x_cord)

        self.assertEqual(captain_commando.x, int(x_cord))
        self.assertEqual(captain_commando.y, int(y_cord))
        self.assertEqual(captain_commando.position, (int(x_cord), int(y_cord)))
        # BLOODIA!
        self.assertEqual(jin.x, int(y_cord))
        self.assertEqual(jin.y, int(x_cord))
        self.assertEqual(jin.position, (int(y_cord), int(x_cord)))

    def test_set_position_FAILURE_case(self):
        """
        Testing the set_position command with inputs that should cause it to EXPLODE.
        This is just to ensure that the type checking remains intact.
        """
        hogwash = Plebian()
        bustah_wolf = Jester()

        x_cord = "Do dogs like to backflip?"
        y_cord = bustah_wolf

        with self.assertRaises(ValueError) as context:
            hogwash.set_position(x_cord, y_cord)

        with self.assertRaises(TypeError) as context:
            hogwash.set_position(y_cord, x_cord)

    """
    set_name tests
    """
    def test_set_name_success_case(self):
        """
        Default set name case. Due to type checking, "ints" are acceptable inputs.
        """
        some_guy = Plebian()
        some_gal = Jester()

        name_one = "Bruce, the Strongest One"
        name_two = 12003100

        # No names should be set yet.
        self.assertEqual(some_guy.name, None)
        self.assertEqual(some_gal.name, None)

        some_guy.set_name(name_one)
        some_gal.set_name(name_two)

        self.assertEqual(some_guy.name, name_one)
        self.assertEqual(some_gal.name, str(name_two))

    """
    character icon tests
    """
    def test_character_icons(self):
        """
        Just some tests to make sure the default character icons are what they should be.
        """
        plebbie_the_plebian = Plebian()
        jestie_the_jester = Jester()

        self.assertEqual(plebbie_the_plebian.icon, "P")
        self.assertEqual(jestie_the_jester.icon, "J")

    """
    movement_action tests for the PLEBIAN class.
    """
    def test_plebian_movement_action_success_case(self):
        """
        Success case for doing the Plebian movement actions. Going to make sure
        they all work.
        """
        epic_plebian = Plebian()
        x_cord = 3
        y_cord = 3
        epic_plebian.set_position(x_cord, y_cord)
        # Test the UP direction.
        for direction in epic_plebian.UP:
            result = epic_plebian.movement_action(direction)
            self.assertEqual(
                result,
                (x_cord, y_cord + 1)
            )
        # Test the DOWN direction.
        for direction in epic_plebian.DOWN:
            result = epic_plebian.movement_action(direction)
            self.assertEqual(
                result,
                (x_cord, y_cord - 1)
            )
        # Test the LEFT direction.
        for direction in epic_plebian.LEFT:
            result = epic_plebian.movement_action(direction)
            self.assertEqual(
                result,
                (x_cord - 1, y_cord)
            )
        # Test the RIGHT direction.
        for direction in epic_plebian.RIGHT:
            result = epic_plebian.movement_action(direction)
            self.assertEqual(
                result,
                (x_cord + 1, y_cord)
            )

    def test_plebian_movement_action_unrecognized_direction_case(self):
        """
        Test the case where the direction specified isn't one that the Plebian
        class doesn't recognize. The Plebian shouldn't end up moving at all.
        """
        epic_plebian = Plebian()
        x_cord = 3
        y_cord = 3
        epic_plebian.set_position(x_cord, y_cord)

        chump_direction = "Go where the wind blows"

        # Shouldn't end up moving anywhere if we don't have a recognized direction.
        result = epic_plebian.movement_action(chump_direction)
        self.assertEqual(
            result,
            (x_cord, y_cord)
        )

    def test_plebian_movement_action_no_x_y_case(self):
        """
        We're going to try to move the Plebian, but in this case we don't have any
        of the x or y values set, so this should result in an error.
        """
        chump_plebian = Plebian()
        chump_direction = "up"

        with self.assertRaises(ValueError) as context:
            result = chump_plebian.movement_action(chump_direction)

            self.assertTrue("Missing an X or Y (or both, heh) value!" in context.exception)

    """
    movement_action tests for the JESTER class.
    """
    def test_jester_movement_action_success_case(self):
        """
        Success case for the Jester movement actions. The movements are less
        straightforward compared to that of the Plebian class.
        """
        epic_jester = Jester()
        x_cord = 8
        y_cord = 8
        epic_jester.set_position(x_cord, y_cord)
        # Test the UP direction.
        for direction in epic_jester.UP:
            result = epic_jester.movement_action(direction)
            self.assertEqual(
                result,
                (x_cord, y_cord + len(direction))
            )
        # Test the DOWN direction.
        for direction in epic_jester.DOWN:
            result = epic_jester.movement_action(direction)
            self.assertEqual(
                result,
                (x_cord, y_cord - len(direction))
            )
        # Test the LEFT direction.
        for direction in epic_jester.LEFT:
            result = epic_jester.movement_action(direction)
            self.assertEqual(
                result,
                (x_cord - len(direction), y_cord)
            )
        # Test the RIGHT direction.
        for direction in epic_jester.RIGHT:
            result = epic_jester.movement_action(direction)
            self.assertEqual(
                result,
                (x_cord + len(direction), y_cord)
            )

    def test_jester_movement_action_unrecognized_direction_case(self):
        """
        Very similar to the Plebian case, except this time it's a Jester.
        Business as usual, baybee?
        """
        epic_jester = Jester()
        x_cord = 8
        y_cord = 8
        epic_jester.set_position(x_cord, y_cord)

        chump_direction = "MEMORIES BROKEN THE TRUTH GOES UNSPOKEN"

        # Shouldn't end up moving anywhere if we don't have a recognized direction.
        result = epic_jester.movement_action(chump_direction)
        self.assertEqual(
            result,
            (x_cord, y_cord)
        )

    def test_jester_movement_action_no_x_y_case(self):
        """
        Again, similar to the Plebian case but in this case we're trying
        to move a Jester that has no x or y..
        """
        chump_jester = Jester()
        chump_direction = "down"

        with self.assertRaises(ValueError) as context:
            result = chump_jester.movement_action(chump_direction)

            self.assertTrue("Missing an X or Y (or both, heh) value!" in context.exception)