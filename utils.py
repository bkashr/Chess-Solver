import chess
from chess_board import display_board

def practice_openings(board):
    print("\nChoose an Opening:")
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

def practice_defenses(board):
    print("\nChoose a Defense:")
    defenses = {
        "1": "Sicilian Defense",
        "2": "French Defense",
        "3": "Caro-Kann Defense",
        "4": "Pirc Defense",
        "5": "Modern Defense",
        "6": "Alekhine Defense"
    }
    for num, defense in defenses.items():
        print(f"{num}. {defense}")

    choice = input("Enter the number of your choice: ")

    defense_moves = {
        "1": ["e4", "c5"],  # Sicilian Defense
        "2": ["e4", "e6"],  # French Defense
        "3": ["e4", "c6"],  # Caro-Kann Defense
        "4": ["e4", "d6"],  # Pirc Defense
        "5": ["e4", "g6"],  # Modern Defense
        "6": ["e4", "Nf6"]  # Alekhine Defense
    }

    if choice in defense_moves:
        moves = defense_moves[choice]
        print(f"\nPracticing {defenses[choice]}...")
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