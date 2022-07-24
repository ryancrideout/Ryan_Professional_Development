import unittest
from unittest.mock import patch

from classes.game import Game
# from classes.plain import Plain
# from classes.maptile import MapTile
from classes.mapengine import MapEngine
from classes.plebian import Plebian
from classes.jester import Jester


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
    # @patch('classes.game.input', create=True) # mocked_input_mapengine, mocked_input_game
    # @patch('classes.mapengine.input', create=True)
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
        # mocked_input_mapengine.side_effect = [
        #     map_width,
        #     map_height,
        #     # Create Character Command
        #     x,
        #     y,
        # ]
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

    # @patch('classes.game.input', create=True) # mocked_input_mapengine, mocked_input_game
    # @patch('classes.mapengine.input', create=True)
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
        # mocked_input_mapengine.side_effect = [
        #     map_width,
        #     map_height,
        # ]
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

    # """
    # set map tests.
    # """
    # def test_set_map_success_case(self):
    #     chump_game = Game()
    #     # New Game should have no map set yet.
    #     self.assertEqual(chump_game.map, None)

    #     # Note that a Plain IS a map. Specifically, a
    #     # Plain is a subclass of Map.
    #     some_plain = Plain()
    #     chump_game.set_map(some_plain)
    #     self.assertEqual(chump_game.map, some_plain)

    # def test_set_map_failure_case(self):
    #     chump_game = Game()
    #     # New Game should have no map set yet.
    #     self.assertEqual(chump_game.map, None)

    #     # Unfortunately we can't attach sexy beasts to games.
    #     with self.assertRaises(TypeError) as context:
    #         chump_game.set_map("Hi I'm a sexy beast.")

    #         self.assertTrue("Unable to attach Map Type obect to Game." in context.exception)

    # """
    # add_entity_to_map tests.
    # """
    # def test_add_entity_to_map_no_map_case(self):
    #     '''
    #     This should fail as we can't add an entity to a map
    #     that doesn't exist.
    #     '''
    #     chump_game = Game()
    #     # Important to note that anyone can be a sexy beast, even the plebians.
    #     sexy_beast = Plebian()

    #     with self.assertRaises(ValueError) as context:
    #         chump_game.add_entity_to_map(sexy_beast)

    #         self.assertTrue("There is no map associated with the game!" in context.exception)

    # def test_add_entity_to_map_non_entity_case(self):
    #     '''
    #     This should fail as we can't add something to the map that does not
    #     have an x and y cordinate.
    #     '''
    #     chump_game = Game()
    #     some_plain = Plain()
    #     some_plain.initialize(10, 10)
    #     chump_game.set_map(some_plain)

    #     with self.assertRaises(AttributeError) as context:
    #         chump_game.add_entity_to_map(42 + 300)

    #         self.assertTrue("'int' object has no attribute 'x'" in context.exception)

    # def test_add_entity_to_map_SUCCESS_case(self):
    #     '''
    #     Default success case. We should be able to add a character to a map, no problems.
    #     '''
    #     chump_game = Game()
    #     some_plain = Plain()
    #     some_plain.initialize(10, 10)
    #     chump_game.set_map(some_plain)

    #     x_cord = 2
    #     y_cord = 2

    #     the_victim = Plebian()
    #     chump_game.set_entity_position(the_victim, x_cord, y_cord)
    #     chump_game.add_entity_to_map(the_victim)

    #     self.assertEqual(
    #         chump_game.map.grid[x_cord][y_cord].occupant,
    #         the_victim
    #     )

    # def test_add_entity_to_map_DUPLICATE_case(self):
    #     '''
    #     We're going to add the same character TWICE to the same map.
    #     Once with the same coordinates, and then once with different coordinates.

    #     The first case should fail (due to two entities being on the same space),
    #     but the second case should pass (due to them being on different spaces).

    #     I'm okay (for now) with the second case passing because maybe there could
    #     be "clones" on the map, but this is worth investigation. And I dunno, it
    #     could get messy.
    #     '''
    #     chump_game = Game()
    #     some_plain = Plain()
    #     some_plain.initialize(10, 10)
    #     chump_game.set_map(some_plain)

    #     x_cord = 2
    #     y_cord = 2

    #     the_victim = Plebian()
    #     chump_game.set_entity_position(the_victim, x_cord, y_cord)
    #     chump_game.add_entity_to_map(the_victim)

    #     self.assertEqual(
    #         chump_game.map.grid[x_cord][y_cord].occupant,
    #         the_victim
    #     )

    #     with self.assertRaises(AttributeError) as context:
    #         chump_game.add_entity_to_map(the_victim)

    #         self.assertTrue("Map space is already occupied!" in context.exception)

    #     # Update the position so we can re-add "the victim" to the map.
    #     chump_game.set_entity_position(the_victim, x_cord + 1, y_cord + 1)
    #     chump_game.add_entity_to_map(the_victim)

    #     self.assertEqual(
    #         chump_game.map.grid[x_cord + 1][y_cord + 1].occupant,
    #         the_victim
    #     )
    #     # Check again to make sure the first "victim" is still on the map.
    #     self.assertEqual(
    #         chump_game.map.grid[x_cord][y_cord].occupant,
    #         the_victim
    #     )

    # def test_add_entity_to_map_OUT_OF_BOUNDS_case(self):
    #     '''
    #     Try to add an entity to a map, but the entity coordinates will
    #     be out of bounds.

    #     We'll get a key error, but maybe there'd be a way to have more
    #     rigorous error checking. Maybe have some checks on the Character class?
    #     Not sure.
    #     '''
    #     chump_game = Game()
    #     some_plain = Plain()
    #     some_plain.initialize(10, 10)
    #     chump_game.set_map(some_plain)

    #     x_cord = 12
    #     y_cord = 12

    #     the_lost_one = Plebian()
    #     chump_game.set_entity_position(the_lost_one, x_cord, y_cord)
    #     with self.assertRaises(KeyError):
    #         chump_game.add_entity_to_map(the_lost_one)

    # """
    # remove_entity_from_map tests.
    # """
    # def test_remove_entity_from_map_SUCCESS_case(self):
    #     '''
    #     Put an entity on a map and then remove it. This should be pretty
    #     straightforward.
    #     '''
    #     chump_game = Game()
    #     some_plain = Plain()
    #     some_plain.initialize(10, 10)
    #     chump_game.set_map(some_plain)

    #     x_cord = 2
    #     y_cord = 2

    #     the_victim = Plebian()
    #     chump_game.set_entity_position(the_victim, x_cord, y_cord)
    #     chump_game.add_entity_to_map(the_victim)

    #     # Now we remove the victim. I feel like I'm some mafia member cleaning the scene.
    #     chump_game.remove_entity_from_map(the_victim)
    #     self.assertEqual(
    #         chump_game.map.grid[x_cord][y_cord].occupant,
    #         None
    #     )

    # @patch('builtins.print')
    # def test_remove_entity_from_map_EMPTY_case(self, mock_print):
    #     '''
    #     Create an entity, but don't add it to the map. We'll try to remove it, but won't
    #     be able to as, well, it just doesn't exist.
    #     '''
    #     chump_game = Game()
    #     some_plain = Plain()
    #     some_plain.initialize(10, 10)
    #     chump_game.set_map(some_plain)

    #     x_cord = 2
    #     y_cord = 2

    #     mr_waffles = Plebian()
    #     chump_game.set_entity_position(mr_waffles, x_cord, y_cord)

    #     chump_game.remove_entity_from_map(mr_waffles)
    #     mock_print.assert_called_with("{}, {} is already empty!".format(x_cord, y_cord))

    # def test_remove_entity_from_map_NO_MAP_case(self):
    #     '''
    #     This should fail, as how can we remove something from a map if a map doesn't exist?

    #     At this point though I feel like I'm testing the compiler more than anything else.
    #     '''
    #     chump_game = Game()

    #     x_cord = 2
    #     y_cord = 2

    #     some_guy = Plebian()
    #     chump_game.set_entity_position(some_guy, x_cord, y_cord)

    #     with self.assertRaises(ValueError) as context:
    #         chump_game.remove_entity_from_map(some_guy)

    #         self.assertTrue("There is no map associated with the game!" in context.exception)

    # def test_remove_entity_from_map_non_entity_case(self):
    #     '''
    #     This will obviously error. I can't think of many cases where this should naturally
    #     occur though.
    #     '''
    #     chump_game = Game()
    #     some_plain = Plain()
    #     some_plain.initialize(10, 10)
    #     chump_game.set_map(some_plain)

    #     with self.assertRaises(AttributeError) as context:
    #         chump_game.remove_entity_from_map(666)

    #         self.assertTrue("'int' object has no attribute 'x'" in context.exception)

    # """
    # check_if_occupied tests.
    # """
    # def test_check_if_occupied_NO_MAP_case(self):
    #     '''
    #     Hard to check if a tile on a map is occupied if there's no map.

    #     I'm sure someone has said this before. Maybe the voices in my head.
    #     '''
    #     chump_game = Game()
    #     x_cord = 2
    #     y_cord = 2
    #     with self.assertRaises(ValueError) as context:
    #         chump_game.check_if_occupied(x_cord, y_cord)

    #         self.assertTrue("There is no map associated with the game!" in context.exception)

    # def test_check_if_occupied_OUT_OF_BOUNDS_case(self):
    #     """
    #     Exactly what is described by the title. We should get a key error.
    #     """
    #     the_game = Game()
    #     smallest_plain = Plain()
    #     smallest_plain.initialize(3, 3)
    #     the_game.set_map(smallest_plain)

    #     x_cord = 40000
    #     y_cord = 40000

    #     with self.assertRaises(KeyError):
    #         the_game.check_if_occupied(x_cord, y_cord)

    # def test_check_if_occupied_FALSE_case(self):
    #     """
    #     Check if an unoccupied square is unoccupied.

    #     Remember, "False" isn't necessarily a bad thing.

    #     "Did you murder this man?"

    #     "False."
    #     """
    #     chump_game = Game()
    #     plane = Plain()
    #     plane.initialize(10, 10)
    #     chump_game.set_map(plane)

    #     x_cord = 8
    #     y_cord = 8

    #     self.assertEqual(
    #         chump_game.check_if_occupied(x_cord, y_cord),
    #         False
    #     )

    # def test_check_if_occupied_TRUE_case(self):
    #     """
    #     Check if an occupied square is occupied.

    #     Note that "True" CAN be a bad thing.

    #     "Did you set your boss's house on fire?"

    #     "True."
    #     """
    #     chump_game = Game()
    #     the_void = Plain()
    #     the_void.initialize(10, 10)
    #     chump_game.set_map(the_void)

    #     x_cord = 3
    #     y_cord = 3

    #     master_of_the_universe = Plebian()
    #     chump_game.set_entity_position(master_of_the_universe, x_cord, y_cord)
    #     chump_game.add_entity_to_map(master_of_the_universe)

    #     self.assertEqual(
    #         chump_game.check_if_occupied(x_cord, y_cord),
    #         True
    #     )

    # """
    # initialize_map tests.
    # """
    # @patch('classes.game.input', create=True)
    # def test_initialize_map_SUCCESS_case(self, mocked_input):
    #     """
    #     Simple case of initializing a map and assigning it to the game.

    #     Note we're going to have to supply user inputs for this.

    #     Furthermore, this is just to make sure the map gets attached to the game,
    #     we can be more rigorous with the "initialize" method on the Maps.
    #     """
    #     x_cord = 10
    #     y_cord = 8
    #     mocked_input.side_effect = [x_cord, y_cord]
    #     a_game = Game()
    #     a_game.initialize_map()

    #     self.assertTrue(isinstance(a_game.map, Plain))
    #     self.assertEqual(a_game.map.width, x_cord)
    #     self.assertEqual(a_game.map.height, y_cord)

    # @patch('classes.game.input', create=True)
    # def test_initialize_map_FAILURE_case(self, mocked_input):
    #     """
    #     Going to crash this method by giving it some string inputs.

    #     This raises the question of maybe we should allow the user to try
    #     again if they input something "dumb", but that might be a later task.
    #     """
    #     x_cord = "ten"
    #     y_cord = "eight"
    #     mocked_input.side_effect = [x_cord, y_cord]
    #     a_game = Game()

    #     with self.assertRaises(ValueError):
    #         a_game.initialize_map()

    """
    create_character tests.
    """
    @patch('classes.game.input', create=True)
    def test_create_character_plebian_case(self, mocked_input):
        """
        Create ourselves a plebian. We'll be sure to give them a great name.
        """
        best_game = Game()
        character_type = "plebian"
        name = "The Fresh Kid"
        mocked_input.side_effect = [character_type, name]

        # Create our character and assert that the class and name is right.
        fresh_meat = best_game.create_character()
        self.assertTrue(isinstance(fresh_meat, Plebian))
        self.assertEqual(fresh_meat.name, name)

    @patch('classes.game.input', create=True)
    def test_create_character_jester_case(self, mocked_input):
        """
        Almost identical to the first test, though in this case we're making a jester.
        """
        best_game = Game()
        character_type = "JeStEr"
        name = "King Snuffles"
        mocked_input.side_effect = [character_type, name]

        # Create our character and assert that the class and name is right.
        not_plebian = best_game.create_character()
        self.assertTrue(isinstance(not_plebian, Jester))
        self.assertEqual(not_plebian.name, name)

    @patch('classes.game.input', create=True)
    def test_create_character_unspecified_case(self, mocked_input):
        """
        The case where we give a character type that's undefined or not known.
        This will give us back a Plebian.
        """
        best_game = Game()
        character_type = "Epic Tier 3 Engineer"
        name = "Isaac Clarke"
        mocked_input.side_effect = [character_type, name]

        # Create our character and assert that the class and name is right.
        engineer = best_game.create_character()
        self.assertTrue(isinstance(engineer, Plebian))
        self.assertEqual(engineer.name, name)

    """
    set_character_position tests.
    """
    @patch('classes.game.input', create=True)
    def test_set_character_position_success_case(self, mocked_input):
        """
        Have a character, and set it's position. Pretty straightforward. I hope.

        Note that the inputs get cast to int, hence the string and int input.

        Also note that setting the character position is independent of the map so
        trying to set a character's position to be outside of map bounds is futile.
        """
        power_game = Game()
        the_coach = Plebian()
        x_cord = "2"
        y_cord = 2
        mocked_input.side_effect = [x_cord, y_cord]

        # Nothing should be set yet.
        self.assertEqual(the_coach.position, None)
        self.assertEqual(the_coach.x, None)
        self.assertEqual(the_coach.y, None)

        power_game.set_character_position(the_coach)

        self.assertEqual(the_coach.position, (int(x_cord), y_cord))
        self.assertEqual(the_coach.x, int(x_cord))
        self.assertEqual(the_coach.y, y_cord)

    def test_set_character_position_NON_CHARACTER_case(self):
        """
        Case where we try to set the character position of a non character.

        This should end in heartbreak and failure.
        """
        power_game = Game()
        with self.assertRaises(TypeError) as context:
            power_game.set_character_position("Big Chungus lives on as the dominant meme")

            self.assertTrue("Cannot set position of non-character object!" in context.exception)

    @patch('classes.game.input', create=True)
    def test_set_character_position_dumb_input_case(self, mocked_input):
        """
        Case where we try some outrageously stupid inputs for the method. Ideally, things should break.
        """
        power_game = Game()
        harvey_dent = Jester()
        x_cord = "War. War never changes."
        y_cord = Game()
        mocked_input.side_effect = [x_cord, y_cord]

        with self.assertRaises(ValueError):
            power_game.set_character_position(harvey_dent)

    """
    move_character tests.
    """
    # @patch('classes.game.input', create=True)
    # @patch('classes.mapengine.input', create=True) # mocked_input_mapengine, mocked_input_game
    @patch('builtins.input', create=True)
    def test_move_character_success_case(self, mocked_input):
        """
        Simple test to see if we can move a character on the map. Note that the movement
        actions are tied to the character classes themselves, so we'll test those more
        rigorously for those tests.
        """
        # Values for mocked user inputs.
        map_width = "10"
        map_height = "10"
        character_type = "plebian"
        character_name = "Isaac"
        char_starting_x = "3"
        char_starting_y = "3"
        up = "up"
        down = "down"
        left = "left"
        right = "right"
        # mocked_input_mapengine.side_effect = [


        # ]
        mocked_input.side_effect = [
            map_width,
            map_height,
            character_type,
            character_name,
            char_starting_x,
            char_starting_y,
            # Need character name to specify who to move
            character_name,
            up,
            character_name,
            down,
            character_name,
            left,
            character_name,
            right,
        ]

        # Set up to put the character on the map
        chump_game = Game()
        the_mapengine = MapEngine()
        chump_game.set_map_engine(the_mapengine)
        the_mapengine.initialize_map()
        plebian_isaac = chump_game.create_character()
        chump_game.set_character_position(plebian_isaac)
        the_mapengine.add_entity_to_map(plebian_isaac)

        # Make sure Isaac is on the map.
        self.assertEqual(
            the_mapengine.map.grid[int(char_starting_x)][int(char_starting_y)].occupant,
            plebian_isaac
        )

        # Move Isaac "Up"
        chump_game.move_character()
        self.assertEqual(
            the_mapengine.map.grid[int(char_starting_x)][int(char_starting_y) + 1].occupant,
            plebian_isaac
        )

        # Move Isaac "Down"
        chump_game.move_character()
        self.assertEqual(
            the_mapengine.map.grid[int(char_starting_x)][int(char_starting_y)].occupant,
            plebian_isaac
        )

        # Move Isaac "Left"
        chump_game.move_character()
        self.assertEqual(
            the_mapengine.map.grid[int(char_starting_x) - 1][int(char_starting_y)].occupant,
            plebian_isaac
        )

        # Move Isaac "Right"
        chump_game.move_character()
        self.assertEqual(
            the_mapengine.map.grid[int(char_starting_x)][int(char_starting_y)].occupant,
            plebian_isaac
        )

    # @patch('classes.game.input', create=True) # mocked_input_mapengine, mocked_input_game
    # @patch('classes.mapengine.input', create=True)
    @patch('builtins.input', create=True)
    def test_move_character_non_existent_character_case(self, mocked_input):
        """
        Try to move a character who just doesn't exist. Big sad.
        """
        # Values for mocked user inputs.
        map_width = "10"
        map_height = "10"
        character_name = "King Darius"
        mocked_input.side_effect = [
            map_width,
            map_height,
            character_name,
        ]
        # mocked_input_game.side_effect = [
        #     character_name,
        # ]

        chump_game = Game()
        the_mapengine = MapEngine()
        chump_game.set_map_engine(the_mapengine)
        the_mapengine.initialize_map()

        with self.assertRaises(ValueError) as context:
            chump_game.move_character()

            self.assertTrue("{} is not a character that exists on the map!".format(character_name) in context.exception)

    # @patch('classes.game.input', create=True) # mocked_input_mapengine, mocked_input_game
    # @patch('classes.mapengine.input', create=True)
    @patch('builtins.input', create=True)
    def test_move_character_already_occupied_case(self, mocked_input):
        """
        Now we try to move a chracter to a spot that is already occupied.

        Obviously we can't move them to that position, just like in real life.
        """
        # Values for mocked user inputs.
        map_width = "10"
        map_height = "10"
        character_1_type = "plebian"
        character_1_name = "Isaac"
        char_1_starting_x = "3"
        char_1_starting_y = "3"
        character_2_type = "jester"
        character_2_name = "Darius"
        char_2_starting_x = "3"
        char_2_starting_y = "4"
        up = "up"
        mocked_input.side_effect = [
            map_width,
            map_height,
            character_1_type,
            character_1_name,
            char_1_starting_x,
            char_1_starting_y,
            character_2_type,
            character_2_name,
            char_2_starting_x,
            char_2_starting_y,
            # Need character name to specify who to move
            character_1_name,
            up,
        ]
        # mocked_input_game.side_effect = [

        # ]

        # Set up to put the character on the map
        chump_game = Game()
        the_mapengine = MapEngine()
        chump_game.set_map_engine(the_mapengine)
        the_mapengine.initialize_map()

        # Add Isaac to the map and make sure he's there.
        plebian_isaac = chump_game.create_character()
        chump_game.set_character_position(plebian_isaac)
        the_mapengine.add_entity_to_map(plebian_isaac)
        self.assertEqual(
            the_mapengine.map.grid[int(char_1_starting_x)][int(char_1_starting_y)].occupant,
            plebian_isaac
        )

        # Add Darius to the map and make sure he's there.
        jester_darius = chump_game.create_character()
        chump_game.set_character_position(jester_darius)
        the_mapengine.add_entity_to_map(jester_darius)
        self.assertEqual(
            the_mapengine.map.grid[int(char_2_starting_x)][int(char_2_starting_y)].occupant,
            jester_darius
        )

        # Attempt to move Isaac up. This shouldn't fly as Darius is already in that spot.
        # As such Isaac should still be in the same spot. Same as Darius, for that matter.
        chump_game.move_character()
        self.assertEqual(
            the_mapengine.map.grid[int(char_1_starting_x)][int(char_1_starting_y)].occupant,
            plebian_isaac
        )
        self.assertEqual(
            the_mapengine.map.grid[int(char_2_starting_x)][int(char_2_starting_y)].occupant,
            jester_darius
        )

    # @patch('classes.game.input', create=True) # mocked_input_mapengine, mocked_input_game
    # @patch('classes.mapengine.input', create=True)
    @patch('builtins.input', create=True)
    def test_move_character_NO_MAP_case(self, mocked_input):
        """
        Try to move a character when we have no map attached to the game. As expected this
        should fail. If not, go order a pizza or something. Maybe? I don't know.
        """
        # Values for mocked user inputs.
        character_type = "plebian"
        character_name = "Isaac"
        char_starting_x = "3"
        char_starting_y = "3"
        up = "up"
        mocked_input.side_effect = [
            character_type,
            character_name,
            char_starting_x,
            char_starting_y,
            # Need character name to specify who to move
            character_name,
            up,
        ]
        # mocked_input_game.side_effect = [

        # ]

        # Set up to put the character on the map
        chump_game = Game()
        the_mapengine = MapEngine()
        chump_game.set_map_engine(the_mapengine)
        plebian_isaac = chump_game.create_character()
        chump_game.set_character_position(plebian_isaac)
        # Normally the error would occur here, but that's not what we're trying to test.
        # chump_game.add_entity_to_map(plebian_isaac)

        with self.assertRaises(ValueError) as context:
            chump_game.move_character()

            self.assertTrue("There is no map associated with the game!" in context.exception)

    # @patch('classes.game.input', create=True) # mocked_input_mapengine, mocked_input_game
    # @patch('classes.mapengine.input', create=True)
    @patch('builtins.input', create=True)
    def test_move_character_OUT_OF_BOUNDS_case(self, mocked_input):
        """
        Try to move a character out of bounds - a message should be printed (though we won't see it),
        but we won't end up moving the character at all.
        """
        # Values for mocked user inputs.
        map_width = "10"
        map_height = "10"
        character_type = "plebian"
        character_name = "Isaac"
        char_starting_x = "0"
        char_starting_y = "0"
        down = "down"
        mocked_input.side_effect = [
            map_width,
            map_height,
            character_type,
            character_name,
            char_starting_x,
            char_starting_y,
            # Need character name to specify who to move
            character_name,
            down,
        ]
        # mocked_input_game.side_effect = [


        # ]

        # Set up to put the character on the map
        chump_game = Game()
        the_mapengine = MapEngine()
        chump_game.set_map_engine(the_mapengine)
        the_mapengine.initialize_map()
        plebian_isaac = chump_game.create_character()
        chump_game.set_character_position(plebian_isaac)
        the_mapengine.add_entity_to_map(plebian_isaac)

        # Make sure Isaac is on the map.
        self.assertEqual(
            the_mapengine.map.grid[int(char_starting_x)][int(char_starting_y)].occupant,
            plebian_isaac
        )

        # Try to move Isaac "Down". He shouldn't end up moving anywhere so his position
        # should stay the same.
        chump_game.move_character()
        self.assertEqual(
            the_mapengine.map.grid[int(char_starting_x)][int(char_starting_y)].occupant,
            plebian_isaac
        )

    # """
    # set_maptile_occupant tests
    # """
    # def test_set_maptile_occupant_success_case(self):
    #     """
    #     Basic success case. If this fails we're in a heap of trouble.
    #     """
    #     heroic_maptile = MapTile()
    #     simply_dan = Plebian()
    #     chump_game = Game()

    #     # No occupant... YET
    #     self.assertEqual(heroic_maptile.occupant, None)

    #     chump_game.set_maptile_occupant(simply_dan, heroic_maptile)

    #     # Now Dan is an occupant.
    #     self.assertEqual(heroic_maptile.occupant, simply_dan)

    # def test_set_maptile_occupant_n0ne_case(self):
    #     """
    #     In my infinite wisdom I forgot that we want to be able to set
    #     the map_occupant to be "None" - a relevant case for when we
    #     remove enities from map.
    #     """
    #     heroic_maptile = MapTile()
    #     simply_dan = Plebian()
    #     chump_game = Game()

    #     # No occupant... YET
    #     self.assertEqual(heroic_maptile.occupant, None)

    #     chump_game.set_maptile_occupant(simply_dan, heroic_maptile)

    #     # Dan is an occupant. All is good.
    #     self.assertEqual(heroic_maptile.occupant, simply_dan)

    #     # Now we don't want the occupant to be anything.
    #     chump_game.set_maptile_occupant(None, heroic_maptile)

    #     # There's nothing here now!
    #     self.assertEqual(heroic_maptile.occupant, None)

    # def test_set_maptile_occupant_FAILURE_case(self):
    #     """
    #     We're going to try setting an occupant that isn't a character or is "None".
    #     This shouldn't fly, though we may have to make adjustments later.
    #     """
    #     heroic_maptile = MapTile()
    #     epic_string = "I am the ember of eternity!"
    #     chump_game = Game()

    #     with self.assertRaises(TypeError) as context:
    #         chump_game.set_maptile_occupant(epic_string, heroic_maptile)

    #         self.assertTrue("Cannot make a non-character a map occupant!" in context.exception)

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
        chump_game = Game()

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
        chump_game.set_entity_position(hugh_jackman, x_cord, y_cord)
        chump_game.set_entity_position(jugh_hackman, y_cord, x_cord)

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
        chump_game = Game()

        x_cord = "21"
        y_cord = "18"

        # SET SOME POSITIONS
        chump_game.set_entity_position(captain_commando, x_cord, y_cord)
        chump_game.set_entity_position(jin, y_cord, x_cord)

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
        chump_game = Game()

        x_cord = "Do dogs like to backflip?"
        y_cord = bustah_wolf

        with self.assertRaises(ValueError) as context:
            chump_game.set_entity_position(hogwash, x_cord, y_cord)

        with self.assertRaises(TypeError) as context:
            chump_game.set_entity_position(hogwash, y_cord, x_cord)

    """
    set_entity_name tests
    """
    def test_set_entity_name_success_case(self):
        """
        Default set name case. Due to type checking, "ints" are acceptable inputs.
        """
        some_guy = Plebian()
        some_gal = Jester()
        chump_game = Game()

        name_one = "Bruce, the Strongest One"
        name_two = 12003100

        # No names should be set yet.
        self.assertEqual(some_guy.name, None)
        self.assertEqual(some_gal.name, None)

        chump_game.set_entity_name(some_guy, name_one)
        chump_game.set_entity_name(some_gal, name_two)

        self.assertEqual(some_guy.name, name_one)
        self.assertEqual(some_gal.name, str(name_two))

    """
    display_game_command tests.
    """
    def test_display_game_commands(self):
        """
        This command is literally just a bunch of print statements, so I'm not quite
        sure how to test this, so I'll just leave it alone for now.
        """
        pass