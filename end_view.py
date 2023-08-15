import tkinter as tk

class EndView(tk.Toplevel):
    def __init__(self, master, word):
        super().__init__(master)
        self.title("Game Over")
        self.geometry("200x100")
        
        if word:
            label = tk.Label(self, text=f"Game Over!\nCorrect word: {word}")
        else:
            label = tk.Label(self, text="Game Over!\nNo correct word guessed.")
        
        label.pack(padx=20, pady=20)