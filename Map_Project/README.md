# How to run this dang game

First of all, you'll need Python to run this, at LEAST Python version 3.9. Probably any version of Python 3 would work, though that's untested. If you need to get a working version of Python, you can download it [here.](https://www.python.org/downloads/)

Once you've got Python installed, you're good to go. Just type `python run_game.py` to run the game and the game will prompt you on what to do.

# Help I've never touched code before how do I run this.

### DISCLAIMER - These instructions are for Windows. I don't develop in Linux and Mac... Mac scares me.

Okay well first thing first you're going to need a console emulator. Personally I like [Cmder](https://cmder.net/), but any console emulator of your choice should work. Here is a [Cmder tutorial](https://www.youtube.com/watch?v=Xm790AkFeK4) if you need it. I didn't watch the whole thing because time is money and I feel that stating that might elicit a smile or a chuckle from whoever reads this.

When you download Cmder (or whatever console emulator), you'll also need Git as well. Cmder has an option to install it with Git, so that's what I recommend. Once you have Git, go to your file directory of choice (E.G., `C:/users/bruce_willis/projects`) and type into the console: `git clone https://github.com/ryancrideout/Ryan_Professional_Development.git`. What you're doing is cloning THIS repository. so you can run the code.

Once you successfully download the repository, go to the `Map_Project` directory and type `python run_game.py` to get started.

# How to run Unittests

While being in the `Map_Project` directory (I.E., this directory), simply run `python -m unittest discover`.

To run unit tests and hide the print statements (I.E., the terminal outputs), add `-b` to the command so you have `python -m unittest discover -b`.

I might have plans in the future to make this something you can do in Pipenv Shell or something, I don't know.
