import chess

def display_board(board):
    """Prints the board in text format."""
    print(board)

def create_board():
    """Creates a new chess board with all pieces."""
    return chess.Board()