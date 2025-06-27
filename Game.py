import tkinter as tk
import subprocess
import os
import sys

def start_game():
    script_path = os.path.join(os.path.dirname(sys.argv[0]), "ram.py")#gets directory where the current script is running
    subprocess.Popen([sys.executable, script_path], creationflags=subprocess.CREATE_NEW_CONSOLE)

# Main Window
root = tk.Tk()
root.title("Game App")
root.geometry("500x400")

# Button to Start Game
start_button = tk.Button(root, text="Start Game", command=start_game, font=("Arial", 14), bg="green", fg="white")
start_button.pack(pady=50)

root.mainloop()