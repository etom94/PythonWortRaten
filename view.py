
### View:

import tkinter as tk

class WordGuessView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.word_vars = []
        
        self.upper_frame = tk.Frame(self)
        self.lower_frame = tk.Frame(self)
        
        self.upper_frame.pack(fill="both", expand=True)
        self.lower_frame.pack(fill="both", expand=True)
        
        self.create_buttons()

    def create_buttons(self):
        for word in self.controller.get_words():
            word_var = tk.StringVar(value=word)  # Direkt den Wert setzen
            self.word_vars.append(word_var)
            button = tk.Button(self.lower_frame, textvariable=word_var)
            button.configure(command=lambda w=word: self.controller.button_clicked(w))
            button.pack(padx=1,pady=1, fill="both", expand=True)
            