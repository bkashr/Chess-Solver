import tkinter as tk
from menu import create_menu
from utils import show_chess_board
from chess_board import create_board
import tkinter.messagebox as messagebox
import sys

def main():
    try:
        print("Starting chess application...")
        
        # Create the main application window
        root = tk.Tk()
        print("Created main window")
        
        # Set the title of the window
        root.title("Chess App")
        
        # Set a minimum size for the window
        root.minsize(600, 400)
        
        # Add an exit button
        exit_button = tk.Button(root, text="Exit", command=root.quit)
        exit_button.pack(side=tk.BOTTOM, pady=10)
        
        # Call the create_menu function to add the menu to the window
        print("Creating menu...")
        create_menu(root)
        print("Menu created")
        
        # Create a new chess board
        print("Creating chess board...")
        board = create_board()
        print("Chess board created")
        
        print("Starting main loop...")
        # Start the Tkinter event loop to run the application
        root.mainloop()
        print("Main loop ended")
        
    except Exception as e:
        print(f"Error starting application: {e}")
        print(f"Error type: {type(e)}")
        import traceback
        traceback.print_exc()
        messagebox.showerror("Error", f"Failed to start application: {e}")

# If this script is run directly (not imported), call the main function
if __name__ == "__main__":
    print("Python version:", sys.version)
    print("Starting main function...")
    main()