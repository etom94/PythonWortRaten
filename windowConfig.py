def configureWindow(root):
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    windowWidth = 400
    windwoHeight = 400

    xPosition = (screenWidth - windowWidth) // 2 
    yPosition = (screenHeight - windwoHeight) // 2

    root.geometry(f"{windowWidth}x{windwoHeight}+{xPosition}+{yPosition}")