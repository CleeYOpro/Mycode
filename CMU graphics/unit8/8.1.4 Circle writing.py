app.nextAngle = 0
app.radius = 140
app.circleFull = False

# circles
Circle(200, 200, 180, fill=None, border='seaGreen', borderWidth=12)
Circle(200, 200, 160, fill='seaGreen')
Circle(200, 200, 90, fill='white')

# center image
Circle(235, 215, 10, fill=None, border='seaGreen', borderWidth=5)
Arc(200, 200, 70, 70, 90, 180, fill='seaGreen')
Line(170, 235, 230, 235, fill='seaGreen', lineWidth=5)
Oval(196, 180, 15, 20, fill='seaGreen', rotateAngle=320)
Oval(204, 180, 15, 20, fill='seaGreen', rotateAngle=40)

def onKeyPress(key):
    # If the circles are not full, draw the text in a ring around the canvas.
    # Use the getPointInDir function with app radius and nextAngle to get
    # the nextX, and nextY for the label.
    if (app.circleFull == False):
        app.nextAngle += 10

        ### Fix Your Code Here ###
        nextX, nextY = getPointInDir(200, 200, app.nextAngle, app.radius)

        # Draws the label in the correct position.
        Label(key, nextX, nextY, fill='white', size=20, bold=True,
              rotateAngle=app.nextAngle)

    # Gets the location of our next ring of words unless the rings are full.
    if (app.nextAngle == 360):
        if (app.radius > 115):
            app.nextAngle = 0
            app.radius -= 25
        else:
            app.circleFull = True
