
### View:

import tkinter as tk

class WordGuessView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.word_vars = []
        self.letter_labels = []

        self.upper_frame = tk.PanedWindow(self, height=200)
        self.lower_frame = tk.PanedWindow(self, orient=tk.VERTICAL)

        self.upper_frame.grid(row=0, column=0)
        self.lower_frame.grid(row=1, column=0)

        self.create_letter_labels()
        self.create_buttons()

    def create_letter_labels(self):
        random_word = self.controller.get_random_word()
        for i, letter in enumerate(random_word):  # Use random_word here
            letter_label = tk.Label(self.upper_frame, text="_", font=("Helvetica", 16)) 
            letter_label.grid(row=0, column=i, sticky='nsew')
            self.letter_labels.append(letter_label)  # Append to letter_labels list

    def create_buttons(self):
        for i, word in enumerate(self.controller.get_random_word_list()):
            word_var = tk.StringVar(value=word)
            self.word_vars.append(word_var)
            button = tk.Button(self.lower_frame, textvariable=word_var)
            button.configure(command=lambda w=word, btn=button: self.controller.button_clicked(w, btn))
            button.grid(row=i // 5, column=i % 5, sticky='nsew')

    def update_word_display(self, revealed_letters):
        for i, revealed in enumerate(revealed_letters):
            if revealed:
                self.letter_labels[i].config(text=self.controller.get_random_word()[i])

    def deactivate_button(self, btn, button_widget):
        button_widget.config(state=tk.DISABLED, bg="black")

          