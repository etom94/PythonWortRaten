
#model.py

class WordGuessModel:
    def __init__(self):
        self.words = self.generate_words()
    
    def generate_words(self):
        return [
        "apple", "banana", "car", "dog", "elephant",
        "flower", "guitar", "house", "ice cream", "jacket",
        "kite", "lion", "mountain", "notebook", "ocean",
        "piano", "queen", "rainbow", "sun", "tree"
    ]
        
        