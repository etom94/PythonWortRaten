import tkinter as tk

class WordGuess(tk.Frame):
    def __init__(self, master, words):
        super().__init__(master)
        self.words = words
        self.create_buttons()
        
    def create_buttons(self):
        for word in self.words:
            button = tk.Button(self, text=word, command=lambda w= word: self.button_clicked(w))
            button.pack()
            
    def button_clicked(self,word):
        print(f"Button '{word}' clicked!")

if __name__ == "__main__":
    words = [
        "apple", "banana", "car", "dog", "elephant",
        "flower", "guitar", "house", "ice cream", "jacket",
        "kite", "lion", "mountain", "notebook", "ocean",
        "piano", "queen", "rainbow", "sun", "tree"
    ]
    
    root = tk.Tk()
    app = WordGuess(root,words)
    app.pack()
    root.mainloop()