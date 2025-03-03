import tkinter as tk
from menu import create_menu

def main():
    # Create the main application window
    root = tk.Tk()
    
    # Set the title of the window
    root.title("Chess App")
    
    # Call the create_menu function to add the menu to the window
    create_menu(root)
    
    # Start the Tkinter event loop to run the application
    root.mainloop()

# If this script is run directly (not imported), call the main function
if __name__ == "__main__":
    main()