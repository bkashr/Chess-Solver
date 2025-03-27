import chess
import tkinter as tk
from tkinterweb import HtmlFrame
from tkinter import messagebox

# Opening database with common openings and their evaluations
OPENING_DATABASE = {
    "Sicilian Defense": {
        "moves": ["e4", "c5"],
        "description": "A sharp, aggressive defense that leads to complex positions.",
        "best_responses": ["Nf3", "d4", "c3"]
    },
    "French Defense": {
        "moves": ["e4", "e6"],
        "description": "A solid, positional defense that aims for a strong pawn structure.",
        "best_responses": ["d4", "Nf3", "c4"]
    },
    "Caro-Kann Defense": {
        "moves": ["e4", "c6"],
        "description": "A solid, classical defense that focuses on piece development.",
        "best_responses": ["d4", "Nf3", "c4"]
    },
    "Pirc Defense": {
        "moves": ["e4", "d6"],
        "description": "A hypermodern defense that allows White to build a strong center.",
        "best_responses": ["d4", "Nf3", "c4"]
    },
    "Halloween Gambit": {
        "moves": ["e4", "e5", "Nf3", "Nc6", "Nxe5", "Nxe5"],
        "description": "An aggressive gambit that sacrifices a knight for initiative.",
        "best_responses": ["d4", "Bc4", "Qh5"]
    }
}

def show_chess_board(board, parent_window=None):
    try:
        print("Starting show_chess_board function...")
        
        # Create a new window for the chess board
        board_window = tk.Toplevel()
        print("Created board window")
        board_window.title("Chess Board")
        
        # Set a minimum size for the window
        board_window.minsize(600, 600)
        print("Set window size")
        
        # Create a frame for the chess board
        board_frame = tk.Frame(board_window)
        print("Created board frame")
        board_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        print("Packed board frame")
        
        # Create a 2D array of labels to represent the chess board
        labels = [[None for _ in range(8)] for _ in range(8)]
        print("Created labels array")

        # Unicode chess pieces with better visibility
        piece_symbols = {
            'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
            'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙'
        }

        # Colors for the board
        light_color = "#F0D9B5"  # Light wood color
        dark_color = "#B58863"   # Dark wood color
        
        # Variables for move selection
        selected_square = None
        selected_label = None
        
        def on_square_click(row, col):
            nonlocal selected_square, selected_label
            
            if selected_square is None:
                # First click - select piece
                square = chess.square(col, 7 - row)
                piece = board.piece_at(square)
                if piece and piece.color == board.turn:
                    selected_square = square
                    selected_label = labels[row][col]
                    # Highlight selected square
                    labels[row][col].config(bg="#7B61FF")  # Purple highlight
            else:
                # Second click - try to move
                target_square = chess.square(col, 7 - row)
                move = chess.Move(selected_square, target_square)
                
                if move in board.legal_moves:
                    board.push(move)
                    update_board()
                    selected_square = None
                    selected_label = None
                else:
                    # Reset selection
                    if selected_label:
                        row, col = chess.square_rank(selected_square), chess.square_file(selected_square)
                        selected_label.config(bg=light_color if (row + col) % 2 == 0 else dark_color)
                    selected_square = None
                    selected_label = None
        
        def update_board():
            for i in range(8):
                for j in range(8):
                    piece = board.piece_at(chess.square(j, 7 - i))
                    if piece:
                        symbol = piece_symbols[piece.symbol()]
                        text_color = "black" if piece.color == chess.BLACK else "#000080"
                        labels[i][j].config(
                            text=symbol,
                            fg=text_color,
                            bg=light_color if (i + j) % 2 == 0 else dark_color
                        )
                    else:
                        labels[i][j].config(
                            text="",
                            bg=light_color if (i + j) % 2 == 0 else dark_color
                        )

        for i in range(8):
            for j in range(8):
                piece = board.piece_at(chess.square(j, 7 - i))
                if piece:
                    symbol = piece_symbols[piece.symbol()]
                    text_color = "black" if piece.color == chess.BLACK else "#000080"
                    labels[i][j] = tk.Label(
                        board_frame,
                        text=symbol,
                        font=('Arial', 36, 'bold'),
                        width=4,
                        height=2,
                        bg=light_color if (i + j) % 2 == 0 else dark_color,
                        fg=text_color
                    )
                else:
                    labels[i][j] = tk.Label(
                        board_frame,
                        width=4,
                        height=2,
                        bg=light_color if (i + j) % 2 == 0 else dark_color
                    )
                labels[i][j].grid(row=i, column=j, padx=0, pady=0)
                labels[i][j].bind('<Button-1>', lambda e, r=i, c=j: on_square_click(r, c))
        
        # Create navigation buttons
        button_frame = tk.Frame(board_window)
        button_frame.pack(pady=10)
        
        def go_back():
            if len(board.move_stack) > 0:
                board.pop()
                update_board()
        
        def exit_board():
            board_window.destroy()
            if parent_window:
                parent_window.destroy()
        
        tk.Button(button_frame, text="Undo Move", command=go_back).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Exit", command=exit_board).pack(side=tk.LEFT, padx=5)
        
        print("Finished creating chess board display")
                
    except Exception as e:
        print(f"Error creating chess board window: {e}")
        print(f"Error type: {type(e)}")
        import traceback
        traceback.print_exc()
        messagebox.showerror("Error", f"Failed to display chess board: {e}")

def practice_defense(board, defense, menu_window):
    print(f"Practicing {defense}")
    
    if defense in OPENING_DATABASE:
        opening_info = OPENING_DATABASE[defense]
        moves = opening_info["moves"]
        description = opening_info["description"]
        best_responses = opening_info["best_responses"]
        
        print(f"\nPracticing {defense}...")
        print(f"Description: {description}")
        print("Best responses:", ", ".join(best_responses))
        
        for move in moves:
            board.push_san(move)
        
        # Close the menu window
        menu_window.destroy()
        
        # Show the board
        show_chess_board(board)
        
        # Show opening information without sound
        info_window = tk.Toplevel()
        info_window.title("Opening Information")
        info_window.geometry("400x200")
        
        info_text = f"{defense}\n\n{description}\n\nBest responses: {', '.join(best_responses)}"
        tk.Label(info_window, text=info_text, wraplength=350).pack(pady=20)
        
        tk.Button(info_window, text="Close", command=info_window.destroy).pack(pady=10)
    else:
        print("Invalid choice.")

def suggest_best_move(board):
    """Analyze the current position and suggest the best move."""
    if board.is_game_over():
        return None, "Game is over!"
    
    # Get legal moves
    legal_moves = list(board.legal_moves)
    if not legal_moves:
        return None, "No legal moves available!"
    
    # Simple evaluation based on piece values
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }
    
    best_move = None
    best_eval = float('-inf')
    
    for move in legal_moves:
        board.push(move)
        eval = 0
        
        # Evaluate the position after the move
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                value = piece_values[piece.piece_type]
                if piece.color == board.turn:
                    eval += value
                else:
                    eval -= value
        
        board.pop()
        
        if eval > best_eval:
            best_eval = eval
            best_move = move
    
    if best_move:
        return best_move, f"Best move: {board.san(best_move)}"
    return None, "Could not determine best move"

def open_play(board):
    print("\nStarting open play mode...")
    
    # Create a new window for open play
    play_window = tk.Toplevel()
    play_window.title("Open Play")
    play_window.minsize(400, 300)
    
    # Create a frame for the input
    input_frame = tk.Frame(play_window)
    input_frame.pack(pady=10)
    
    # Create entry field for moves
    move_entry = tk.Entry(input_frame, width=20)
    move_entry.pack(side=tk.LEFT, padx=5)
    
    # Create a label for status
    status_label = tk.Label(play_window, text="Enter your move (or 'q' to quit, 'h' for hint)")
    status_label.pack(pady=5)
    
    def make_move():
        move = move_entry.get()
        move_entry.delete(0, tk.END)  # Clear the entry field
        
        if move.lower() == "q":
            play_window.destroy()
            return
        elif move.lower() == "h":
            best_move, message = suggest_best_move(board)
            status_label.config(text=message)
            return
            
        try:
            board.push_san(move)
            show_chess_board(board)
            status_label.config(text="Move successful! Enter your next move.")
        except ValueError:
            status_label.config(text="Invalid move. Try again.")
    
    # Create a button to make the move
    move_button = tk.Button(input_frame, text="Make Move", command=make_move)
    move_button.pack(side=tk.LEFT, padx=5)
    
    # Bind Enter key to make_move
    move_entry.bind('<Return>', lambda e: make_move())
    
    # Show the initial board
    show_chess_board(board)
    
    # Wait for the window to be closed
    play_window.wait_window()
    
    print("\nGame Over!")
    print("Result:", board.result())