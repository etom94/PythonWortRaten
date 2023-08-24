
### View:

import tkinter as tk

class WordGuessView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.word_vars = []
        self.letter_labels = []

        self.header_frame = tk.PanedWindow(self)
        self.upper_frame = tk.PanedWindow(self, height=200)
        self.lower_frame = tk.PanedWindow(self, orient=tk.VERTICAL)
        self.footer_frame = tk.PanedWindow(self)

        self.header_frame.grid(row=0, column=0)
        self.upper_frame.grid(row=1, column=0, pady=10)
        self.lower_frame.grid(row=2, column=0, pady=5)
        self.footer_frame.grid(row=4, column=0, pady=20)

        self.create_header()
        self.create_letter_labels()
        self.create_buttons()
        
    def create_footer(self, initial_tries):
        self.tries_left = (initial_tries+5)
        point_label = tk.Label(self.footer_frame, text=f"Tries: {self.tries_left}")
        point_label.grid(row=0, column=0, sticky='nsew')
        self.point_label = point_label  # Store the label as an instance variable

        
    def update_tries(self):
        self.tries_left -= 1
        self.point_label.config(text=f"Tries: {self.tries_left}")
        
    def create_header(self):
        titel_label = tk.Label(self.header_frame, text="Guess the right Word", font=('Helvetica', 12))
        titel_label.grid(row=0, column=0, sticky='nsew')

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
            button.grid(row=i // 5, column=i % 5, sticky='nsew', padx=2, pady=2)

    def update_word_display(self, revealed_letters):
        for i, revealed in enumerate(revealed_letters):
            if revealed:
                self.letter_labels[i].config(text=self.controller.get_random_word()[i])

    def deactivate_button(self, btn, button_widget):
        button_widget.config(state=tk.DISABLED, bg="black")
        

          