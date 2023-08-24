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
        word_list = random.sample(self.words, 30)
        if selected_word not in word_list:
            word_list.pop()
            word_list.append(selected_word)
        random.shuffle(word_list)
        return word_list
        
    def get_random_word(self):
        return self.selected_word
    
    def get_random_word_list(self):
        return self.random_word_list
    
    def get_revealed_letters(self,random_word, selected_word):
        revealed_letters = [letter1 == letter2 for letter1, letter2 in zip(random_word, selected_word)]
        return revealed_letters

    def words_list(self):
        return [
            'development', 'software', 'internet', 'computer', 'interaction', 'collaboration', 'project', 
             'enthusiasm', 'opportunity', 'knowledgeable', 'technology', 'innovation', 'knowledge', 'programming', 
             'learning', 'creative', 'solution', 'experience', 'developer', 'framework', 'industry', 'algorithm', 
             'education', 'coding', 'web', 'application', 'interface', 'resource', 'function', 'analysis', 'practice', 
             'challenge', 'effort', 'progress', 'advancement', 'curiosity', 'achievement', 'passion', 'together', 
             'enthusiastic', 'communication', 'community', 'efficiency', 'inspiration', 'platform', 'Apple', 'Table', 
             'Elephant', 'Guitar', 'Window', 'Ocean', 'Butterfly', 'Candle', 'Diamond', 'Sunshine', 'Mountain', 'Rainbow', 
             'Keyboard', 'Flower', 'Moonlight', 'Coffee', 'Dolphin', 'Castle', 'Pillow', 'Firefly', 'Telescope', 'River', 
             'Sandcastle', 'Starfish', 'Turtle', 'Backpack', 'Lemonade', 'Whisper', 'Adventure', 'Balloon', 'Dragonfly', 'Echo', 
             'Friendship', 'Harmony', 'Island', 'Jellyfish', 'Koala', 'Lighthouse', 'Meadow', 'Nightingale', 'Octopus', 'Penguin', 
             'Quilt', 'Seashell', 'Thunder', 'Umbrella', 'Vacation', 'Waterfall', 'Xylophone'
             ]
