import chess
import tkinter as tk
from utils import show_chess_board

def display_board(board):
    """Prints the board in text format."""
    print(board)

def create_board():
    """Creates a new chess board with all pieces."""
    return chess.Board()

def main():
    # Create the main application window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Create a new chess board
    board = create_board()

    # Display the chess board
    show_chess_board(board)

    # Start the Tkinter event loop to run the application
    root.mainloop()

# If this script is run directly (not imported), call the main function
if __name__ == "__main__":
    main()