import chess
import tkinter as tk
from tkinterweb import HtmlFrame

def show_chess_board(board):
    # Create a new window for the chess board
    board_window = tk.Toplevel()
    board_window.title("Chess Board")

    # Create a frame for the chess board
    board_frame = HtmlFrame(board_window, messages_enabled=False)
    board_frame.pack(pady=20)

    # Load the board image
    board_svg = "chess-pieces-master/boards/8x8_pink_1Kbyte_gambit.svg"
    with open(board_svg, 'r') as file:
        board_svg_content = file.read()

    # Display the board image
    board_frame.load_html(board_svg_content)

    # Load images for the chess pieces
    piece_images = {
        'r': "chess-pieces-master/chess_1Kbyte_gambit/bR.svg",
        'n': "chess-pieces-master/chess_1Kbyte_gambit/bN.svg",
        'b': "chess-pieces-master/chess_1Kbyte_gambit/bB.svg",
        'q': "chess-pieces-master/chess_1Kbyte_gambit/bQ.svg",
        'k': "chess-pieces-master/chess_1Kbyte_gambit/bK.svg",
        'p': "chess-pieces-master/chess_1Kbyte_gambit/bP.svg",
        'R': "chess-pieces-master/chess_1Kbyte_gambit/wR.svg",
        'N': "chess-pieces-master/chess_1Kbyte_gambit/wN.svg",
        'B': "chess-pieces-master/chess_1Kbyte_gambit/wB.svg",
        'Q': "chess-pieces-master/chess_1Kbyte_gambit/wQ.svg",
        'K': "chess-pieces-master/chess_1Kbyte_gambit/wK.svg",
        'P': "chess-pieces-master/chess_1Kbyte_gambit/wP.svg"
    }

    # Create a 2D array of labels to represent the chess board
    labels = [[None for _ in range(8)] for _ in range(8)]

    for i in range(8):
        for j in range(8):
            piece = board.piece_at(chess.square(j, 7 - i))
            if piece:
                piece_svg = piece_images[piece.symbol()]
                with open(piece_svg, 'r') as file:
                    piece_svg_content = file.read()
                piece_frame = HtmlFrame(board_frame, messages_enabled=False)
                piece_frame.load_html(piece_svg_content)
                labels[i][j] = piece_frame
            else:
                labels[i][j] = tk.Label(board_frame, width=8, height=4, bg="white" if (i + j) % 2 == 0 else "gray")
            labels[i][j].grid(row=i, column=j)

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
        show_chess_board(board)  # Show the chess board in a new window
    else:
        print("Invalid choice.")

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