
### Controller:

import view
from end_view import EndView

class WordGuessController:
    def __init__(self, root, model):
        self.root = root
        self.count = 0
        self.model = model
        self.view = view.WordGuessView(root, self)
        self.view.create_buttons()
        self.view.create_footer(initial_tries=self.count)
    
    def get_random_word(self):
        return self.model.get_random_word()
    
    def get_random_word_list(self):
        return self.model.get_random_word_list()

    def button_clicked(self, word, button_widget):
        random_word = self.get_random_word()
        self.count += 1
        if random_word == word or self.count >= 5:
            self.view.destroy()
            text = "Congratulations! The winning word was: "
            if self.count >= 5:
                text = "Better Luck next time! The winning word was: "
            # Dann rufen Sie die neue View auf
            end_view = EndView(self.root, random_word, text)
            end_view.grid(row=0, column=0)
        else:
            revealed_letters = self.model.get_revealed_letters(random_word, word)
            self.view.update_tries()
            self.view.update_word_display(revealed_letters)
            self.view.deactivate_button(word, button_widget)

