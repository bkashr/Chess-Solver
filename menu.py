import tkinter as tk
from chess_board import create_board
from utils import practice_openings, practice_defenses, open_play

def create_menu(root):
    board = create_board()  # Creates a new board with all pieces

    def start_practice_openings():
        practice_openings(board)
    
    def start_practice_defenses():
        practice_defenses(board)
    
    def start_open_play():
        open_play(board)

    menu_frame = tk.Frame(root)
    menu_frame.pack(pady=20)

    tk.Label(menu_frame, text="Choose an option:").pack()
    tk.Button(menu_frame, text="Practice Openings", command=start_practice_openings).pack(pady=5)
    tk.Button(menu_frame, text="Practice Defenses", command=start_practice_defenses).pack(pady=5)
    tk.Button(menu_frame, text="Open Play", command=start_open_play).pack(pady=5)