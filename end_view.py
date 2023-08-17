import tkinter as tk

class EndView(tk.Frame):
    def __init__(self, master, winning_word):
        super().__init__(master)
        
        self.winning_word = winning_word
        
        # Hier gestaltest du den Inhalt deiner neuen View
        label = tk.Label(self, text=f"Congratulations! The winning word was: {winning_word}", font=("Helvetica", 16))
        label.pack(padx=20, pady=20)
        
        # Weitere Widgets und Layout-Elemente hinzufügen, wie du möchtest
