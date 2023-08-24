def configureWindow(root):
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    windowWidth = 500
    windwoHeight = 350

    xPosition = (screenWidth - windowWidth) // 2 
    yPosition = (screenHeight - windwoHeight) // 2

    root.geometry(f"{windowWidth}x{windwoHeight}+{xPosition}+{yPosition}")