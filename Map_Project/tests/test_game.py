import unittest
from classes.game import Game
from classes.plain import Plain
from classes.plebian import Plebian

class TestGame(unittest.TestCase):
    '''
    NOTE: We're going to have to figure out how to do user inputs for
          unit tests.

          Reference this:
          https://stackoverflow.com/questions/47690020/python-3-unit-tests-with-user-input
    '''
    def test_run(self):
        # Should test this last as this depends on EVERYTHING else.
        pass

    def test_set_map_success_case(self):
        chump_game = Game()
        # New Game should have no map set yet.
        self.assertEqual(chump_game.map, None)

        # Note that a Plain IS a map. Specifically, a
        # Plain is a subclass of Map.
        some_plain = Plain()
        chump_game.set_map(some_plain)
        self.assertEqual(chump_game.map, some_plain)

    def test_set_map_failure_case(self):
        chump_game = Game()
        # New Game should have no map set yet.
        self.assertEqual(chump_game.map, None)

        # Unfortunately we can't attach sexy beasts to games.
        with self.assertRaises(TypeError) as context:
            chump_game.set_map("Hi I'm a sexy beast.")

            self.assertTrue("Unable to attach Map Type obect to Game." in context.exception)

    def test_add_entity_to_map_no_map_case(self):
        '''
        This should fail as we can't add an entity to a map
        that doesn't exist.
        '''
        chump_game = Game()
        # Important to note that anyone can be a sexy beast, even the plebians.
        sexy_beast = Plebian()

        with self.assertRaises(ValueError) as context:
            chump_game.add_entity_to_map(sexy_beast)

            self.assertTrue("There is no map associated with the game!" in context.exception)

    def test_add_entity_to_map_non_entity_case(self):
        '''
        This should fail as we can't add something to the map that does not
        have an x and y cordinate.
        '''
        chump_game = Game()
        some_plain = Plain()
        some_plain.initialize(10, 10)
        chump_game.set_map(some_plain)

        with self.assertRaises(AttributeError) as context:
            chump_game.add_entity_to_map(42 + 300)

            self.assertTrue("'int' object has no attribute 'x'" in context.exception)

    def test_remove_entity_to_map(self):
        pass

    def test_check_if_occupied(self):
        pass

    def test_initialize_map(self):
        pass

    def test_create_character(self):
        pass

    def test_set_character_position(self):
        pass

    def test_move_character(self):
        pass

    def test_display_game_commands(self):
        pass