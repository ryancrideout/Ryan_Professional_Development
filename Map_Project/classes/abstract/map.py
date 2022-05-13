from abc import ABC, abstractmethod

class Map(ABC):
    @abstractmethod
    def __init__(self):
        self.width = None
        self.height = None
        self.grid = None

    @abstractmethod
    def initialize(self, width, height):
        print("MAKE A MAP YOU FOOL")

    @abstractmethod
    def render(self):
        print("We're going to have to print out the map here.")