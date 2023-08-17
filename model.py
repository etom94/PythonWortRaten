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
        return ["technology", "programming", "development", "innovation", "community", "knowledge", "creative", "learning", "solution", "software",
        "internet", "computer", "education", "algorithm", "application", "framework", "communication", "platform", "industry", "developer",
        "inspiration", "opportunity", "experience", "collaboration", "coding", "interface", "project", "resource", "web", "function",
        "analysis", "practice", "challenge", "efficiency", "effort", "enthusiastic", "progress", "advancement", "curiosity", "achievement",
        "passion", "together", "enthusiasm", "interaction", "knowledgeable", "platform", "technology", "inspiration", "coding", "learning",
        "community", "efficiency", "communication", "innovation", "creative", "programming", "solution", "experience", "framework", "web",
        "developer", "industry", "algorithm", "education", "opportunity", "challenge", "application", "interface", "resource", "analysis",
        "practice", "function", "project", "progress", "advancement", "curiosity", "achievement", "passion", "effort", "enthusiastic",
        "efficiency", "collaboration", "together", "inspiration", "knowledge", "experience", "technology", "programming", "solution",
        "communication", "learning", "creative", "developer", "framework", "industry", "education", "algorithm", "application", "coding",
        "interface", "web", "project", "resource", "function", "analysis", "practice", "challenge", "effort", "progress", "advancement",
        "curiosity", "achievement", "passion", "enthusiasm", "innovation", "opportunity", "communication", "community", "knowledgeable",
        "efficiency", "platform", "inspiration", "creative", "learning", "programming", "solution", "experience", "framework", "developer",
        "industry", "algorithm", "education", "coding", "web", "application", "interface", "resource", "function", "analysis", "practice",
        "challenge", "effort", "progress", "advancement", "curiosity", "achievement", "passion", "together", "enthusiastic",
        "communication", "technology", "innovation", "knowledge", "programming", "learning", "creative", "solution", "experience",
        "developer", "framework", "industry", "algorithm", "education", "coding", "web", "application", "interface", "resource", "function",
        "analysis", "practice", "challenge", "effort", "progress", "advancement", "curiosity", "achievement", "passion", "together",
        "enthusiastic", "communication", "community", "efficiency", "inspiration", "platform", "inspiration", "coding", "learning",
        "community", "efficiency", "communication", "innovation", "creative", "programming", "solution", "experience", "framework", "web",
        "developer", "industry", "algorithm", "education", "opportunity", "challenge", "application", "interface", "resource", "analysis",
        "practice", "function", "project", "progress", "advancement", "curiosity", "achievement", "passion", "effort", "enthusiastic",
        "efficiency", "collaboration", "together", "inspiration", "knowledge", "experience", "technology", "programming", "solution",
        "communication", "learning", "creative", "developer", "framework", "industry", "education", "algorithm", "application", "coding",
        "interface", "web", "project", "resource", "function", "analysis", "practice", "challenge", "effort", "progress", "advancement",
        "curiosity", "achievement", "passion", "enthusiasm", "innovation", "opportunity", "communication", "community", "knowledgeable",
        "efficiency", "platform", "inspiration", "creative", "learning", "programming", "solution", "experience", "framework", "developer",
        "industry", "algorithm", "education", "coding", "web", "application", "interface", "resource", "function", "analysis", "practice",
        "challenge", "effort", "progress", "advancement", "curiosity", "achievement", "passion", "together", "enthusiastic",
        "communication", "technology", "innovation", "knowledge", "programming", "learning", "creative", "solution", "experience",
        "developer", "framework", "industry", "algorithm", "education", "coding", "web", "application", "interface", "resource", "function",
        "analysis", "practice", "challenge", "effort", "progress", "advancement", "curiosity", "achievement", "passion", "together",
        "enthusiastic", "communication", "community", "efficiency", "inspiration", "platform"
        ]
