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

# Actually run this blasted thing.
if __name__ == "__main__":
    main()