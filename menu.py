import tkinter as tk
from chess_board import create_board
from utils import practice_defense, open_play

def create_menu(root):
    board = create_board()  # Creates a new board with all pieces

    def show_defenses_menu():
        print("Showing defenses menu")  # Debugging statement
        # Clear the current menu
        for widget in root.winfo_children():
            widget.destroy()

        # Create a new frame for the defenses menu
        defenses_frame = tk.Frame(root)
        defenses_frame.pack(pady=20)

        tk.Label(defenses_frame, text="Choose a Defense:").pack()

        defenses = {
            "1": "Sicilian Defense",
            "2": "French Defense",
            "3": "Caro-Kann Defense",
            "4": "Pirc Defense",
            "5": "Halloween Gambit"
        }

        for num, defense in defenses.items():
            tk.Button(defenses_frame, text=defense, command=lambda d=defense: practice_defense(board, d)).pack(pady=5)

        tk.Button(defenses_frame, text="Back", command=lambda: create_menu(root)).pack(pady=5)

    def start_open_play():
        print("Starting open play")  # Debugging statement
        open_play(board)

    # Clear the current menu
    for widget in root.winfo_children():
        widget.destroy()

    menu_frame = tk.Frame(root)
    menu_frame.pack(pady=20)

    tk.Label(menu_frame, text="Choose an option:").pack()
    tk.Button(menu_frame, text="Practice Defenses", command=show_defenses_menu).pack(pady=5)
    tk.Button(menu_frame, text="Open Play", command=start_open_play).pack(pady=5)