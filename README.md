# Coin Toss Game

This program simulates a coin toss game using Python and the tkinter library. It allows the user to guess whether the outcome of a coin flip will be heads or tails, and it keeps track of the user's guesses and the coin flip results. The game provides a graphical interface for user interaction, displaying images of heads and tails during the coin flip.

## Dependencies

- random
- tkinter
- PIL (Pillow) for image processing
- os for file system operations

## Classes

- `coin`: A class representing a coin object with two sides (Heads and Tails).

### Methods

- `flip()`: Flips the coin and updates the coin's side.
- `getHistory()`: Returns the history of coin flips.
- `__str__()`: Returns the current side of the coin.

## Functions

- `results()`: Displays the user's results after the game is finished.
- `playButtons()`: Displays the 'Play again?' buttons.
- `playAgain(YN)`: Determines whether to restart the game or show the results based on the user's choice.
- `callSame(yn)`: Determines whether to make the same call again or ask to play again.
- `click(side)`: Handles the user's coin side call and displays the outcome of the coin flip.
- `subtitle()`: Updates the subtitle text in the interface.
- `buttons()`: Displays the heads and tails buttons.
- `open()`: Initiates the game.

## Usage

1. Create a tkinter window.
2. Initialize a coin object.
3. Load images of heads and tails.
4. Create and configure tkinter widgets (labels, buttons, etc.).
5. Define functions for handling user interactions and updating the interface.
6. Start the tkinter main event loop.