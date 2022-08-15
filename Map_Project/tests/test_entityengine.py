import unittest
from unittest.mock import patch

from classes.jester import Jester
from classes.plebian import Plebian
from classes.engines.entityengine import EntityEngine


class TestEntityEngine(unittest.TestCase):
    """
    create_character tests.
    """
    @patch('builtins.input', create=True)
    def test_create_character_plebian_case(self, mocked_input):
        """
        Create ourselves a plebian. We'll be sure to give them a great name.
        """
        best_entityengine = EntityEngine()
        character_type = "plebian"
        name = "The Fresh Kid"
        mocked_input.side_effect = [character_type, name]

        # Create our character and assert that the class and name is right.
        fresh_meat = best_entityengine.create_character()
        self.assertTrue(isinstance(fresh_meat, Plebian))
        self.assertEqual(fresh_meat.name, name)

    @patch('builtins.input', create=True)
    def test_create_character_jester_case(self, mocked_input):
        """
        Almost identical to the first test, though in this case we're making a jester.
        """
        best_entityengine = EntityEngine()
        character_type = "JeStEr"
        name = "King Snuffles"
        mocked_input.side_effect = [character_type, name]

        # Create our character and assert that the class and name is right.
        not_plebian = best_entityengine.create_character()
        self.assertTrue(isinstance(not_plebian, Jester))
        self.assertEqual(not_plebian.name, name)

    @patch('builtins.input', create=True)
    def test_create_character_unspecified_case(self, mocked_input):
        """
        The case where we give a character type that's undefined or not known.
        This will give us back a Plebian.
        """
        best_entityengine = EntityEngine()
        character_type = "Epic Tier 3 Engineer"
        name = "Isaac Clarke"
        mocked_input.side_effect = [character_type, name]

        # Create our character and assert that the class and name is right.
        engineer = best_entityengine.create_character()
        self.assertTrue(isinstance(engineer, Plebian))
        self.assertEqual(engineer.name, name)

    """
    set_character_position tests.
    """
    @patch('builtins.input', create=True)
    def test_set_character_position_success_case(self, mocked_input):
        """
        Have a character, and set it's position. Pretty straightforward. I hope.

        Note that the inputs get cast to int, hence the string and int input.

        Also note that setting the character position is independent of the map so
        trying to set a character's position to be outside of map bounds is futile.
        """
        power_entityengine = EntityEngine()
        the_coach = Plebian()
        x_cord = "2"
        y_cord = 2
        mocked_input.side_effect = [x_cord, y_cord]

        # Nothing should be set yet.
        self.assertEqual(the_coach.position, None)
        self.assertEqual(the_coach.x, None)
        self.assertEqual(the_coach.y, None)

        power_entityengine.set_character_position(the_coach)

        self.assertEqual(the_coach.position, (int(x_cord), y_cord))
        self.assertEqual(the_coach.x, int(x_cord))
        self.assertEqual(the_coach.y, y_cord)

    def test_set_character_position_NON_CHARACTER_case(self):
        """
        Case where we try to set the character position of a non character.

        This should end in heartbreak and failure.
        """
        power_entityengine = EntityEngine()
        with self.assertRaises(TypeError) as context:
            power_entityengine.set_character_position("Big Chungus lives on as the dominant meme")

            self.assertTrue("Cannot set position of non-character object!" in context.exception)

    @patch('builtins.input', create=True)
    def test_set_character_position_dumb_input_case(self, mocked_input):
        """
        Case where we try some outrageously stupid inputs for the method. Ideally, things should break.
        """
        power_entityengine = EntityEngine()
        harvey_dent = Jester()
        x_cord = "War. War never changes."
        y_cord = EntityEngine()
        mocked_input.side_effect = [x_cord, y_cord]

        with self.assertRaises(ValueError):
            power_entityengine.set_character_position(harvey_dent)

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
        chump_entityengine = EntityEngine()

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
        chump_entityengine.set_entity_position(hugh_jackman, x_cord, y_cord)
        chump_entityengine.set_entity_position(jugh_hackman, y_cord, x_cord)

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
        chump_entityengine = EntityEngine()

        x_cord = "21"
        y_cord = "18"

        # SET SOME POSITIONS
        chump_entityengine.set_entity_position(captain_commando, x_cord, y_cord)
        chump_entityengine.set_entity_position(jin, y_cord, x_cord)

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
        chump_entityengine = EntityEngine()

        x_cord = "Do dogs like to backflip?"
        y_cord = bustah_wolf

        with self.assertRaises(ValueError) as context:
            chump_entityengine.set_entity_position(hogwash, x_cord, y_cord)

        with self.assertRaises(TypeError) as context:
            chump_entityengine.set_entity_position(hogwash, y_cord, x_cord)

    """
    set_entity_name tests
    """
    def test_set_entity_name_success_case(self):
        """
        Default set name case. Due to type checking, "ints" are acceptable inputs.
        """
        some_guy = Plebian()
        some_gal = Jester()
        chump_entityengine = EntityEngine()

        name_one = "Bruce, the Strongest One"
        name_two = 12003100

        # No names should be set yet.
        self.assertEqual(some_guy.name, None)
        self.assertEqual(some_gal.name, None)

        chump_entityengine.set_entity_name(some_guy, name_one)
        chump_entityengine.set_entity_name(some_gal, name_two)

        self.assertEqual(some_guy.name, name_one)
        self.assertEqual(some_gal.name, str(name_two))
