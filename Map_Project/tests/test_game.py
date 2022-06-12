import unittest
from unittest.mock import patch
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

    """
    set map tests.
    """
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

    """
    add_entity_to_map tests.
    """
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

    def test_add_entity_to_map_SUCCESS_case(self):
        '''
        Default success case. We should be able to add a character to a map, no problems.
        '''
        chump_game = Game()
        some_plain = Plain()
        some_plain.initialize(10, 10)
        chump_game.set_map(some_plain)

        x_cord = 2
        y_cord = 2

        the_victim = Plebian()
        the_victim.set_position(x_cord, y_cord)
        chump_game.add_entity_to_map(the_victim)

        self.assertEqual(
            chump_game.map.grid[x_cord][y_cord].occupant,
            the_victim
        )

    def test_add_entity_to_map_DUPLICATE_case(self):
        '''
        We're going to add the same character TWICE to the same map. 
        Once with the same coordinates, and then once with different coordinates.

        The first case should fail (due to two entities being on the same space),
        but the second case should pass (due to them being on different spaces).

        I'm okay (for now) with the second case passing because maybe there could
        be "clones" on the map, but this is worth investigation. And I dunno, it
        could get messy.
        '''
        chump_game = Game()
        some_plain = Plain()
        some_plain.initialize(10, 10)
        chump_game.set_map(some_plain)

        x_cord = 2
        y_cord = 2

        the_victim = Plebian()
        the_victim.set_position(x_cord, y_cord)
        chump_game.add_entity_to_map(the_victim)

        self.assertEqual(
            chump_game.map.grid[x_cord][y_cord].occupant,
            the_victim
        )

        with self.assertRaises(AttributeError) as context:
            chump_game.add_entity_to_map(the_victim)

            self.assertTrue("Map space is already occupied!" in context.exception)

        # Update the position so we can re-add "the victim" to the map.
        the_victim.set_position(x_cord + 1, y_cord + 1)
        chump_game.add_entity_to_map(the_victim)

        self.assertEqual(
            chump_game.map.grid[x_cord + 1][y_cord + 1].occupant,
            the_victim
        )
        # Check again to make sure the first "victim" is still on the map.
        self.assertEqual(
            chump_game.map.grid[x_cord][y_cord].occupant,
            the_victim
        )

    def test_add_entity_to_map_OUT_OF_BOUNDS_case(self):
        '''
        Try to add an entity to a map, but the entity coordinates will
        be out of bounds.

        We'll get a key error, but maybe there'd be a way to have more
        rigorous error checking. Maybe have some checks on the Character class?
        Not sure.
        '''
        chump_game = Game()
        some_plain = Plain()
        some_plain.initialize(10, 10)
        chump_game.set_map(some_plain)

        x_cord = 12
        y_cord = 12

        the_lost_one = Plebian()
        the_lost_one.set_position(x_cord, y_cord)
        with self.assertRaises(KeyError):
            chump_game.add_entity_to_map(the_lost_one)

    """
    remove_entity_from_map tests.
    """
    def test_remove_entity_from_map_SUCCESS_case(self):
        '''
        Put an entity on a map and then remove it. This should be pretty
        straightforward.
        '''
        chump_game = Game()
        some_plain = Plain()
        some_plain.initialize(10, 10)
        chump_game.set_map(some_plain)

        x_cord = 2
        y_cord = 2

        the_victim = Plebian()
        the_victim.set_position(x_cord, y_cord)
        chump_game.add_entity_to_map(the_victim)

        # Now we remove the victim. I feel like I'm some mafia member cleaning the scene.
        chump_game.remove_entity_from_map(the_victim)
        self.assertEqual(
            chump_game.map.grid[x_cord][y_cord].occupant,
            None
        )

    @patch('builtins.print')
    def test_remove_entity_from_map_EMPTY_case(self, mock_print):
        '''
        Create an entity, but don't add it to the map. We'll try to remove it, but won't
        be able to as, well, it just doesn't exist.
        '''
        chump_game = Game()
        some_plain = Plain()
        some_plain.initialize(10, 10)
        chump_game.set_map(some_plain)

        x_cord = 2
        y_cord = 2

        mr_waffles = Plebian()
        mr_waffles.set_position(x_cord, y_cord)

        chump_game.remove_entity_from_map(mr_waffles)
        mock_print.assert_called_with("{}, {} is already empty!".format(x_cord, y_cord))

    def test_remove_entity_from_map_NO_MAP_case(self):
        '''
        This should fail, as how can we remove something from a map if a map doesn't exist?

        At this point though I feel like I'm testing the compiler more than anything else.
        '''
        chump_game = Game()

        x_cord = 2
        y_cord = 2

        some_guy = Plebian()
        some_guy.set_position(x_cord, y_cord)

        with self.assertRaises(ValueError) as context:
            chump_game.remove_entity_from_map(some_guy)

            self.assertTrue("There is no map associated with the game!" in context.exception)

    def test_remove_entity_from_map_non_entity_case(self):
        '''
        This will obviously error. I can't think of many cases where this should naturally
        occur though.
        '''
        chump_game = Game()
        some_plain = Plain()
        some_plain.initialize(10, 10)
        chump_game.set_map(some_plain)

        with self.assertRaises(AttributeError) as context:
            chump_game.remove_entity_from_map(666)

            self.assertTrue("'int' object has no attribute 'x'" in context.exception)

    """
    check_if_occupied tests.
    """
    def test_check_if_occupied_NO_MAP_case(self):
        '''
        Hard to check if a tile on a map is occupied if there's no map.

        I'm sure someone has said this before. Maybe the voices in my head.
        '''
        chump_game = Game()
        x_cord = 2
        y_cord = 2
        with self.assertRaises(ValueError) as context:
            chump_game.check_if_occupied(x_cord, y_cord)

            self.assertTrue("There is no map associated with the game!" in context.exception)

    def test_check_if_occupied_OUT_OF_BOUNDS_case(self):
        """
        Exactly what is described by the title. We should get a key error.
        """
        the_game = Game()
        smallest_plain = Plain()
        smallest_plain.initialize(3, 3)
        the_game.set_map(smallest_plain)

        x_cord = 40000
        y_cord = 40000

        with self.assertRaises(KeyError):
            the_game.check_if_occupied(x_cord, y_cord)

    def test_check_if_occupied_FALSE_case(self):
        """
        Check if an unoccupied square is unoccupied.

        Remember, "False" isn't necessarily a bad thing.

        "Did you murder this man?"

        "False."
        """
        chump_game = Game()
        plane = Plain()
        plane.initialize(10, 10)
        chump_game.set_map(plane)

        x_cord = 8
        y_cord = 8

        self.assertEqual(
            chump_game.check_if_occupied(x_cord, y_cord),
            False
        )
        
    def test_check_if_occupied_TRUE_case(self):
        """
        Check if an occupied square is occupied.

        Note that "True" CAN be a bad thing.

        "Did you set your boss's house on fire?"

        "True."
        """
        chump_game = Game()
        the_void = Plain()
        the_void.initialize(10, 10)
        chump_game.set_map(the_void)

        x_cord = 3
        y_cord = 3

        master_of_the_universe = Plebian()
        master_of_the_universe.set_position(x_cord, y_cord)
        chump_game.add_entity_to_map(master_of_the_universe)

        self.assertEqual(
            chump_game.check_if_occupied(x_cord, y_cord),
            True
        )

    """
    initialize_map tests.
    """
    @patch('classes.game.input', create=True)
    def test_initialize_map_SUCCESS_case(self, mocked_input):
        """
        Simple case of initializing a map and assigning it to the game.

        Note we're going to have to supply user inputs for this.

        Furthermore, this is just to make sure the map gets attached to the game,
        we can be more rigorous with the "initialize" method on the Maps.
        """
        x_cord = 10
        y_cord = 8
        mocked_input.side_effect = [x_cord, y_cord]
        a_game = Game()
        a_game.initialize_map()

        self.assertTrue(isinstance(a_game.map, Plain))
        self.assertEqual(a_game.map.width, x_cord)
        self.assertEqual(a_game.map.height, y_cord)

    @patch('classes.game.input', create=True)
    def test_initialize_map_FAILURE_case(self, mocked_input):
        """
        Going to crash this method by giving it some string inputs.

        This raises the question of maybe we should allow the user to try
        again if they input something "dumb", but that might be a later task.
        """
        x_cord = "ten"
        y_cord = "eight"
        mocked_input.side_effect = [x_cord, y_cord]
        a_game = Game()
        
        with self.assertRaises(ValueError):
            a_game.initialize_map()

    """
    create_character tests.
    """
    def test_create_character(self):
        # Test Two
        pass

    """
    set_character_position tests.
    """
    def test_set_character_position(self):
        pass

    """
    move_character tests.
    """
    def test_move_character(self):
        pass

    """
    display_game_command tests.
    """
    def test_display_game_commands(self):
        pass