import chess
import sys

def display_board(board):
    """Prints the board in text format."""
    print(board)

def main():
    board = chess.Board()  # Creates a new board with all pieces
    display_board(board)  # Shows the board

    print("\nChoose an option:")
    print("1. Practice Openings & Defenses")
    print("2. Open Play")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        practice_openings_defenses(board)
    elif choice == "2":
        open_play(board)
    else:
        print("Invalid choice. Exiting.")
        sys.exit()

def practice_openings_defenses(board):
    print("\nChoose an Opening or Defense:")
    openings = {
        "1": "Ruy Lopez",
        "2": "Sicilian Defense",
        "3": "French Defense",
        "4": "Caro-Kann Defense",
        "5": "Queen's Gambit",
        "6": "Halloween Gambit"
    }
    for num, opening in openings.items():
        print(f"{num}. {opening}")

    choice = input("Enter the number of your choice: ")

    opening_moves = {
        "1": ["e4", "e5", "Nf3", "Nc6", "Bb5"],  # Ruy Lopez
        "2": ["e4", "c5"],  # Sicilian Defense
        "3": ["e4", "e6"],  # French Defense
        "4": ["e4", "c6"],  # Caro-Kann Defense
        "5": ["d4", "d5", "c4"],  # Queen's Gambit
        "6": ["e4", "e5", "Nf3", "Nf6", "Nxe5", "Nc6", "Nxc6"]  # Halloween Gambit
    }

    if choice in opening_moves:
        moves = opening_moves[choice]
        print(f"\nPracticing {openings[choice]}...")
        for move in moves:
            board.push_san(move)  # Apply each move
        display_board(board)  # Show updated board
    else:
        print("Invalid choice.")

def open_play(board):
    print("\nStarting open play mode...")
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

if __name__ == "__main__":
    main()
