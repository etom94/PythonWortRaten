#model.py

import random

class WordGuessModel:
    def __init__(self):
        self.words = self.words_list()
        self.selected_word = self.select_word()
        self.random_word_list = self.generate_random_words(self.selected_word)
        
    def select_word(self):
        selected_word = random.choice(self.words)
        return selected_word
    
    def generate_random_words(self, selected_word):
        word_list = random.sample(self.words, 20)
        if selected_word not in word_list:
            word_list.pop()
            word_list.append(selected_word)
        random.shuffle(word_list)
        return word_list
    
    def words_list(self):
        return [
            "apple", "banana", "car", "dog", "elephant",
            "flower", "guitar", "house", "ice cream", "jacket",
            "kite", "lion", "mountain", "notebook", "ocean",
            "piano", "queen", "rainbow", "sun", "tree"
        ]
        
    def get_random_word(self):
        return self.selected_word
    
    def get_random_word_list(self):
        return self.random_word_list
    
    def get_revealed_letters(self,random_word, selected_word):
        revealed_letters = [letter1 == letter2 for letter1, letter2 in zip(random_word, selected_word)]
        return revealed_letters

