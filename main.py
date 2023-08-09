
### Main:

import tkinter as tk
import model
import controller

if __name__ == "__main__":

    root = tk.Tk()
    model = model.WordGuessModel()
    controller = controller.WordGuessController(root, model)
    controller.view.pack()
    root.mainloop()
    