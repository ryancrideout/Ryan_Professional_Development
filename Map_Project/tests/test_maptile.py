import unittest

from classes.maptile import MapTile
from classes.plebian import Plebian


class TestMapTile(unittest.TestCase):
    """
    set_coordinates tests
    """
    def test_set_coordinates_success_case(self):
        """
        Successfully test the set_coordinates method. At least I hope I'm
        successfully testing it. Someone else can be the judge I suppose.
        """
        the_best_maptile = MapTile()
        x_cord = 40000
        y_cord = 2

        # Nothing should be set.
        self.assertEqual(the_best_maptile.x, None)
        self.assertEqual(the_best_maptile.y, None)
        self.assertEqual(the_best_maptile.coordinates, None)

        the_best_maptile.set_coordinates(x_cord, y_cord)

        # Now we should have everything set.
        self.assertEqual(the_best_maptile.x, x_cord)
        self.assertEqual(the_best_maptile.y, y_cord)
        self.assertEqual(the_best_maptile.coordinates, (x_cord, y_cord))

    def test_set_coordinates_CAST_TO_INT_case(self):
        """
        A test where we cast some strings to integers. This is all in the interest of including some
        type checking for the MapTile class.
        """
        the_best_maptile = MapTile()
        x_cord = "20"
        y_cord = "15"

        # Nothing should be set.
        self.assertEqual(the_best_maptile.x, None)
        self.assertEqual(the_best_maptile.y, None)
        self.assertEqual(the_best_maptile.coordinates, None)

        the_best_maptile.set_coordinates(x_cord, y_cord)

        # Values should be integers, or we riot.
        self.assertEqual(the_best_maptile.x, int(x_cord))
        self.assertEqual(the_best_maptile.y, int(y_cord))
        self.assertEqual(the_best_maptile.coordinates, (int(x_cord), int(y_cord)))

    def test_set_coordinates_FAILURE_case(self):
        """
        This is where we do some dumb inputs, and ensure that we can't set the MapTile
        because of it.
        """
        the_best_maptile = MapTile()
        # 'False' actually works as it evaluates to '0'... though I can't think of many
        # cases where we'd be passing in Boolean values.
        x_cord = False
        y_cord = "The Bear Who Nods His Head"

        with self.assertRaises(ValueError) as context:
            the_best_maptile.set_coordinates(x_cord, y_cord)

    # """
    # set_occupant tests
    # """
    # def test_set_occupant_success_case(self):
    #     """
    #     Basic success case. If this fails we're in a heap of trouble.
    #     """
    #     heroic_maptile = MapTile()
    #     simply_dan = Plebian()

    #     # No occupant... YET
    #     self.assertEqual(heroic_maptile.occupant, None)

    #     heroic_maptile.set_occupant(simply_dan)

    #     # Now Dan is an occupant.
    #     self.assertEqual(heroic_maptile.occupant, simply_dan)

    # def test_set_occupant_n0ne_case(self):
    #     """
    #     In my infinite wisdom I forgot that we want to be able to set
    #     the map_occupant to be "None" - a relevant case for when we
    #     remove enities from map.
    #     """
    #     heroic_maptile = MapTile()
    #     simply_dan = Plebian()

    #     # No occupant... YET
    #     self.assertEqual(heroic_maptile.occupant, None)

    #     heroic_maptile.set_occupant(simply_dan)

    #     # Dan is an occupant. All is good.
    #     self.assertEqual(heroic_maptile.occupant, simply_dan)

    #     # Now we don't want the occupant to be anything.
    #     heroic_maptile.set_occupant(None)

    #     # There's nothing here now!
    #     self.assertEqual(heroic_maptile.occupant, None)

    # def test_set_occupant_FAILURE_case(self):
    #     """
    #     We're going to try setting an occupant that isn't a character or is "None".
    #     This shouldn't fly, though we may have to make adjustments later.
    #     """
    #     heroic_maptile = MapTile()
    #     epic_string = "I am the ember of eternity!"

    #     with self.assertRaises(TypeError) as context:
    #         heroic_maptile.set_occupant(epic_string)

    #         self.assertTrue("Cannot make a non-character a map occupant!" in context.exception)
