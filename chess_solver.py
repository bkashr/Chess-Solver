import tkinter as tk
from menu import create_menu

def main():
    root = tk.Tk()
    root.title("Chess App")
    create_menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()