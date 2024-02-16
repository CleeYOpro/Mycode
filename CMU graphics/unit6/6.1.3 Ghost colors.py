app.background = 'black'

# buttons
cyanButton = Circle(100, 350, 20, fill='cyan')
magentaButton = Circle(200, 350, 20, fill='magenta')
yellowButton = Circle(300, 350, 20, fill='yellow')

ghost = Group(
    Circle(200, 150, 100, fill="black"),
    Rect(100, 150, 200, 100, fill='black'),
    Circle(125, 250, 25,fill="black"),
    Circle(175, 250, 25,fill="black"),
    Circle(225, 250, 25,fill="black"),
    Circle(275, 250, 25,fill="black")
    )

# ghost eyes
Circle(150, 150, 20)
Circle(250, 150, 20)

def onMousePress(mouseX, mouseY):
    # If the mouse clicks on a color button, the ghost should change color
    # accordingly.
    if cyanButton.contains(mouseX, mouseY)==True:
        ghost.fill='cyan'
    if magentaButton.contains(mouseX, mouseY)==True:
        ghost.fill='magenta'
    if yellowButton.contains(mouseX, mouseY)==True:
        ghost.fill='yellow'
    pass
