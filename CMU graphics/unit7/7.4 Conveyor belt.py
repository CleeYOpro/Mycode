app.background = gradient('steelBlue', 'lightSlateGray', start='top')
app.stepsPerSecond = 15

def createWheels(sideWheels, start):
    for i in range(6):
        sideWheels.add(
            Star(start + i * 20, 265, 10, 7, roundness=20),
            Circle(start + i * 20, 265, 6, fill='grey', border='black')
            )

# conveyor belts
Line(10, 290, 390, 290, lineWidth=30, dashes=(2, 40))
Rect(-10, 255, 420, 20, fill='grey', border='black')
rightWheels = Group()
leftWheels = Group()
createWheels(rightWheels, 292)
createWheels(leftWheels, 8)

leftDots = Group()
rightDots = Group()

# machine
Polygon(150, 135, 250, 135, 235, 100, 235, 0, 165, 0, 165, 100,
        fill=gradient('lightGrey', 'grey', start='left-top'))
Line(165, 100, 235, 100, fill='grey')
Rect(116, 135, 168, 200, fill=gradient('lightGrey', 'grey', start='left-top'))
Rect(135, 265, 65, 60, fill=gradient('lightGrey', 'dimGrey', start='left-top'))
Oval(240, 260, 60, 30, fill=gradient('lightGrey', 'dimGrey', start='left-top'))
Line(220, 300, 260, 300, fill=gradient('silver', 'dimGrey', start='left-top'),
     lineWidth=70, dashes=(10, 5))
Line(114, 200, 114, 280, fill='dimGrey', lineWidth=4)
Line(286, 200, 286, 280, fill='dimGrey', lineWidth=4)
Line(115, 330, 285, 330, fill='dimGrey', lineWidth=10)
Rect(135, 150, 130, 60, border='dimGrey')

arrow = Line(160, 180, 240, 180, fill='crimson')

def onKeyPress(key):
    if (key == 'left'):
        arrow.arrowStart = True
    if (key == 'right'):
        arrow.arrowEnd = True

def onKeyRelease(key):
    if (key == 'left'):
        arrow.arrowStart = False
    if (key == 'right'):
        arrow.arrowEnd = False

def onStep():
    # Rotates the wheels of the belts.
    for wheel in leftWheels.children:
        wheel.rotateAngle -= 5
    for wheel in rightWheels.children:
        wheel.rotateAngle += 5

    # Add dots based on which direction the arrow points.
    ### (HINT: Use the values for arrow.arrowStart and arrow.arrowEnd.)
    if arrow.arrowStart == True:
        leftDots.add(Circle(120, 250,5, fill = 'springGreen'))
    if arrow.arrowEnd == True:
        rightDots.add(Circle(280, 250,5, fill = 'deepSkyBlue'))


    # Move the dots in their respective directions by 10 pixels and remove
    # them once they are off-screen.
    ### Place Your Code Here ###
    for b in leftDots.children:
        if b.right <= 0:
            leftDots.remove(b)
        else:
            b.centerX-=10
    for b in rightDots.children:
        if b.left >=400:
            leftDots.remove(b)
        else:
            b.centerX+=10
    pass
