from classes.plain import Plain

class Game():
    def run(self):
        """
        Okay we're going to have to figure out how to initialize this whole thing...
        But that's a problem for later?
        """
        # Make a plain. We can implement logic later to choose our map type.
        plain = Plain()
        # Make this a user input
        plain.initialize(10, 10)
        # Yay this works
        plain.render()

        # TODO: Flesh this out some more, actually make this a "game",
        #       ask user for prompts and then add characters and then
        #       make them move.