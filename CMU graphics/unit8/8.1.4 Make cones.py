app.background = 'black'

lines = Group()
Circle(200, 200, 125, fill=None, border='lime')

def makeCone(numberOfLines):
    stepAngle = 360 / numberOfLines
    for i in range(numberOfLines):
        # Define the angle variable so it equals 'i' times the stepAngle.
        ### Fix Your Code Here ###
        angle = i*stepAngle

        # Define the getPointInDir function 'centered' so it uses a radius of 125.
        ### Fix Your Code Here ###
        x1, y1 = getPointInDir(200, 200, angle, 125)

        # Adds a new line to the group lines using the variables defined.
        lines.add(
            Line(x1, y1, 200, 200, fill='lime')
            )

def onMouseMove(mouseX, mouseY):
    # Loop through each line in the group lines and set their x2, y2 to the
    # mouseX, mouseY.
    for line in lines.children:
        line.x2=mouseX
        line.y2=mouseY
    pass

##### Place your code above this line, code below is for testing purposes #####
# test case:
makeCone(20)
