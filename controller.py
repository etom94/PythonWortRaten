
### Controller:

import view
import end_view

class WordGuessController:
    def __init__(self, root, model):
        self.model = model
        self.view = view.WordGuessView(root, self)
        self.view.create_buttons()
    
    def get_random_word(self):
        return self.model.get_random_word()
    
    def get_random_word_list(self):
        return self.model.get_random_word_list()

    def button_clicked(self, word, button_widget):
        random_word = self.get_random_word()
        if random_word == word:
            end_view.EndView(self.view, random_word)
        else:
            revealed_letters = self.model.get_revealed_letters(random_word, word)
            self.view.update_word_display(revealed_letters)
            self.view.deactivate_button(word, button_widget)

