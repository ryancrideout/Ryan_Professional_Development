import unittest

from classes.plain import Plain
from classes.maptile import MapTile


class TestPlain(unittest.TestCase):
    '''
    Tests for our plain class. I'm really not sure how I'll end up
    testing the render method though.
    '''
    def test_initialize_success_case(self):
        """
        Simple success case. We'll make a plain and make sure the
        attributes are set and that it has maptiles.
        """
        width = 5
        height = 8
        big_plain = Plain()

        # Nothing has been set yet.
        self.assertEqual(big_plain.width, None)
        self.assertEqual(big_plain.height, None)
        self.assertEqual(big_plain.grid, None)

        big_plain.initialize(width, height)

        self.assertEqual(big_plain.width, 5)
        self.assertEqual(big_plain.height, 8)
        for i in range(width):
            for j in range(height):
                self.assertTrue(
                    isinstance(
                        big_plain.grid[i][j],
                        MapTile
                    )
                )

    def test_initialize_FAILURE_case(self):
        """
        Attempt to give the plain non-sensical width and height inputs.
        I don't think I'll be blowing anyone's mind by saying this should
        fail.
        """
        width = "My dog is the cutest dog."
        height = "No no your dog, MY dog."
        big_plain = Plain()

        with self.assertRaises(TypeError) as context:
            big_plain.initialize(width, height)
