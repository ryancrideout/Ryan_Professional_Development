"""
Things to do:
- Create a Game Class
- Create an abstract Map Class
  - Make a "Plain" Subsclass
- Create an abstract Character Class
  - Make some character classes
- Cleanup, put these into folders and stuff.
"""

from abc import ABC, abstractmethod

class Game():
    def shoryuken():
        print("Shoryuken")

class Map(ABC):
    @abstractmethod
    def shin_shoryuken():
        print("Shin Shoryuken")

# The main function where everything starts.
def main():
    print("I am the duke now.")

# Actually run this blasted thing.
if __name__ == "__main__":
    main()