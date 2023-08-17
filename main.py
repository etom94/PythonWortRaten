# main.py

import tkinter as tk
import model
import controller
import windowConfig  # Import the window configuration module

if __name__ == "__main__":
    root = tk.Tk()
    
    # Configure the window using the imported function
    windowConfig.configureWindow(root)
    
    model = model.WordGuessModel()
    controller = controller.WordGuessController(root, model)
    controller.view.pack()
    
    root.mainloop()
