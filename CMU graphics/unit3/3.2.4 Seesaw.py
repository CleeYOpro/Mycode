app.background = 'lightCyan'

# seesaw support
Oval(200, 330, 300, 50, fill='moccasin'),
RegularPolygon(200, 290, 70, 3, fill=None, border='tomato', borderWidth=7)
Circle(200, 235, 15, fill='skyBlue')

# seesaw body
seesaw = Line(50, 235, 350, 235, fill='tomato', lineWidth=12)

# message
message = Label('Balanced', 200, 100, fill='salmon', size=20)

def onMouseMove(mouseX, mouseY):
    # If the mouse is on the right side of the canvas, increase the seesaw's
    # rotateAngle by 1. Otherwise decrease it.
    if (mouseX<200):
        seesaw.rotateAngle-= 1
    else:
        seesaw.rotateAngle+=1

    if (seesaw.rotateAngle <= 0):
        message.value = 'Leaning Left'
    else:
        message.value = 'Leaning Right'
    if (seesaw.rotateAngle==0):
        message.value = 'Balanced'

    if (seesaw.rotateAngle >= 45):
        seesaw.rotateAngle = 45
    if (seesaw.rotateAngle <= -45):
        seesaw.rotateAngle = -45
    pass
