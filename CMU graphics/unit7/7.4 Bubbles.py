app.background = gradient('lightCyan', 'lightSkyBlue', start='bottom')

# grass
Oval(370, 440, 800, 200, fill='mediumSeaGreen')
Oval(130, 450, 800, 200, fill='forestGreen')

def drawDaisy(x, y):
    daisy = Group()

    # Draw the petals of the daisy using 6 Ovals. Each oval should have a
    # width of 9 and a height of 30. Use a loop to figure out the rotateAngle.
    for i in range(6):
        daisy.add(Oval(x, y, 9, 30, rotateAngle = i*30, fill = 'white'))

    # This draws the center piece and adjusts the height so that it looks like
    # the flower is flat on the ground.
    daisy.add(Circle(x, y, 7.5, fill='gold'))
    daisy.height = 20

# Adds daisies to the field.
drawDaisy(2, 365)
drawDaisy(30, 380)
drawDaisy(80, 365)
drawDaisy(114, 369)
drawDaisy(150, 389)
drawDaisy(94, 373)
drawDaisy(164, 376)
drawDaisy(205, 380)
drawDaisy(228, 358)
drawDaisy(330, 383)
drawDaisy(318, 399)
drawDaisy(365, 384)
drawDaisy(399, 399)
drawDaisy(67, 399)
drawDaisy(48, 403)
drawDaisy(269, 363)

bubbleWand = Group(
    Line(100, 300, 125, 325, fill='grey', lineWidth=3),
    Oval(90, 290, 28, 13, fill=None, border='grey', borderWidth=3, rotateAngle=45),
    Oval(90, 290, 33, 16, fill=None, border='grey', borderWidth=4, rotateAngle=45,
         dashes=(3, 2))
    )

bubbles = Group()

def createBubble(x, y):
    bubble = Group(
        Circle(x, y, 20, fill=gradient('white', 'lightBlue', start='top-right'),
               border='white', opacity=50),
        Oval(x + 10, y - 10, 10, 5, fill='white', rotateAngle=45),
        Circle(x + 14, y - 2, 2, fill='white')
        )
    bubbles.add(bubble)

def onMousePress(mouseX, mouseY):
    createBubble(mouseX, mouseY)

def onMouseMove(mouseX, mouseY):
    bubbleWand.centerX = mouseX
    bubbleWand.centerY = mouseY

def onStep():
    # Increase the size of the bubbles and move them up by 0.5 pixels. If a
    # bubble gets too big (a width of at least 100 pixels), remove it.
    for bubble in bubbles.children:
        bubble.width+=0.5
        bubble.height+=0.5
        bubble.centerY-=0.5
        if bubble.width>100:
            bubbles.remove(bubble)
    pass
