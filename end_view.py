
#end_view

import tkinter as tk

class EndView(tk.Frame):
    def __init__(self, root, winning_word, text):
        super().__init__(root)
        
        self.winning_word = winning_word
        
        label = tk.Label(self, text=f"{text} {winning_word}", font=("Helvetica", 12))
        label.pack(padx=20, pady=20)

        # Fügen Sie diese Zeile hinzu, um die Ansicht im Hauptfenster anzuzeigen
        self.grid(row=0, column=0)

        

