import unittest

from classes.game import Game
from classes.jester import Jester
from classes.plebian import Plebian
from classes.engines.entityengine import EntityEngine

"""
Note that here we're just testing the character classes in general here -
I don't think there's enough difference between the character classes to 
warrant separate test files.
"""
class TestCharacters(unittest.TestCase):
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
        chump_entityengine = EntityEngine()
        x_cord = 3
        y_cord = 3
        chump_entityengine.set_entity_position(epic_plebian, x_cord, y_cord)
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
        chump_entityengine = EntityEngine()
        x_cord = 3
        y_cord = 3
        chump_entityengine.set_entity_position(epic_plebian, x_cord, y_cord)

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
        chump_entityengine = EntityEngine()
        x_cord = 8
        y_cord = 8
        chump_entityengine.set_entity_position(epic_jester, x_cord, y_cord)
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
        chump_entityengine = EntityEngine()
        x_cord = 8
        y_cord = 8
        chump_entityengine.set_entity_position(epic_jester, x_cord, y_cord)

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