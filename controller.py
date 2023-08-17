
### Controller:

import view
from end_view import EndView

class WordGuessController:
    def __init__(self, root, model):
        self.count = 0
        self.model = model
        self.view = view.WordGuessView(root, self)
        self.view.create_buttons()
    
    def get_random_word(self):
        return self.model.get_random_word()
    
    def get_random_word_list(self):
        return self.model.get_random_word_list()

    def button_clicked(self, word, button_widget):
        random_word = self.get_random_word()
        self.count +=1
        if random_word == word or self.count == 5:
            # Hier rufst du die neue View auf
            end_view = EndView(self.master, random_word)  # Erstelle eine Instanz der neuen View
            end_view.grid(row=0, column=0)  # Zeige die neue View im Hauptfenster an
        else:
            revealed_letters = self.model.get_revealed_letters(random_word, word)
            self.view.update_word_display(revealed_letters)
            self.view.deactivate_button(word, button_widget)

