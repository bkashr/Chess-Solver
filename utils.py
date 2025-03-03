import chess
import tkinter as tk
from chess_board import display_board

def practice_defense(board, defense):
    print(f"Practicing {defense}")  # Debugging statement
    defense_moves = {
        "Sicilian Defense": ["e4", "c5"],
        "French Defense": ["e4", "e6"],
        "Caro-Kann Defense": ["e4", "c6"],
        "Pirc Defense": ["e4", "d6"],
        "Halloween Gambit": ["e4", "e5", "Nf3", "Nc6", "Nxe5", "Nxe5"]
    }

    if defense in defense_moves:
        moves = defense_moves[defense]
        print(f"\nPracticing {defense}...")  # Debugging statement
        for move in moves:
            board.push_san(move)  # Apply each move
        display_board(board)  # Show updated board
        show_chess_board(board)  # Show the chess board in a new window
    else:
        print("Invalid choice.")

def show_chess_board(board):
    # Create a new window for the chess board
    board_window = tk.Toplevel()
    board_window.title("Chess Board")

    # Create a frame for the chess board
    board_frame = tk.Frame(board_window)
    board_frame.pack(pady=20)

    # Display the chess board
    board_str = str(board)
    for row in board_str.split('\n'):
        tk.Label(board_frame, text=row).pack()

def open_play(board):
    print("\nStarting open play mode...")  # Debugging statement
    while not board.is_game_over():
        print(board)
        move = input("Enter your move (or 'q' to quit): ")
        if move.lower() == "q":
            break
        try:
            board.push_san(move)  # Apply the move
        except ValueError:
            print("Invalid move. Try again.")

    print("\nGame Over!")
    print("Result:", board.result())