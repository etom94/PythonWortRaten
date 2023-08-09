
### Controller:

import view

class WordGuessController:
    def __init__(self, root, model):
        self.model = model
        self.view = view.WordGuessView(root, self)
        self.view.create_buttons()

    def get_words(self):
        return self.model.words

    def button_clicked(self, word):
        print(f"Button '{word}' clicked!")
        
        