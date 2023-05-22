This code is a Python implementation of the Tic-Tac-Toe game using the minimax algorithm for AI-based gameplay. The program allows a user to play against the computer or load a predefined board from a file. The main components of the code include:

The move class represents a move on the Tic-Tac-Toe board with row and column coordinates.
The TicTacToe class contains the game logic and functions for board initialization, printing the board, checking for available moves, evaluating the game status, implementing the minimax algorithm, and finding the best move for both the player and the opponent.
The load_board function reads a board from a file and returns it as a NumPy array.
The main function handles the command-line arguments, initializes the game with the provided board (if any), and starts the gameplay by calling the play_game method of the TicTacToe class.
The code demonstrates how to use the minimax algorithm to create a computer player that plays optimally in the Tic-Tac-Toe game. It evaluates all possible moves and selects the best move based on the predicted outcome.

To play the game, you can run the code with the following optional command-line arguments:

-f or --file: Specify a file to load a board from.
-p or --player: Choose the player that plays first, either 1 (player) or -1 (opponent).
The final board and the winner are displayed after the game ends.

Note: The code assumes that the NumPy library is installed.
