def configureWindow(root):
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    windowWidth = 600
    windwoHeight = 600

    xPosition = (screenWidth - windowWidth) // 2 
    yPosition = (screenHeight - windwoHeight) // 2

    root.geometry(f"{windowWidth}x{windwoHeight}+{xPosition}+{yPosition}")