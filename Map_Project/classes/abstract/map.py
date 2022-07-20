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
