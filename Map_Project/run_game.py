"""
Things to do:
- Create a Game Class
- Create an abstract Map Class
  - Make a "Plain" Subsclass
- Create a MapTile Class
- Create an abstract Character Class
  - Make some character classes
- Cleanup, put these into folders and stuff.
"""
from abc import ABC, abstractmethod

from classes.game import Game


# The main function where everything starts.
def main():
    map_game = Game()
    map_game.run()
    # Should characters have a maptile object?
    # What about the map they're on?
    # Maybe I could just give them a "position" attribute...
    # But even so, moving them is going to require the map (maptiles plural) to be updated.
    # MAYBE I PUT "MOVE CHARACTERS" on the map command?
    # I think maybe we let the game handle all of that, and then it updates the map accordingly.
    # Ugh that's going to be messy.

    # Okay new plan - let the game handle movement, but the player classes will have instructions
    # on how to move.

# Actually run this blasted thing.
if __name__ == "__main__":
    main()