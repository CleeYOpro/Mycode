# background
Rect(190, 0, 10, 400)
Rect(200, 0, 10, 400, fill='tan')

def drawFootstep(x, y, color):
    Oval(x, y - 5, 22, 40, fill=color)
    Circle(x, y + 20, 8, fill=color)
    Rect(x, y + 13, 16, 3, fill='white', align='center')

def onMousePress(mouseX, mouseY):
    # Draw a black footstep if the click is on left half, tan footstep otherwise.
    if mouseX>200:
        drawFootstep(mouseX, mouseY, 'tan')
    else:
        drawFootstep(mouseX, mouseY, 'black')
    pass
