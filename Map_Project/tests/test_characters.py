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
