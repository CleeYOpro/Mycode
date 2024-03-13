app.background = 'thistle'

Rect(200, 200, 275, 355, opacity=30, align='center')
Rect(200, 200, 270, 350, fill='lightGrey', align='center')
Rect(200, 200, 250, 330, fill='ghostWhite', align='center')
Circle(200, 240, 77, opacity=90)
Circle(200, 238, 75, fill='grey')
Circle(200, 225, 75, fill='lightGrey')

Label('Thermostat', 200, 75, fill='dimGrey', size=30, font='montserrat', bold=True)
thermostatLine = Line(200, 225, 200, 150, fill='dimGrey', lineWidth=3)

def drawThermostatLabels():
    for i in range(9):
        angle = 240 + i * 30
        x, y = getPointInDir(200, 235, angle, 100)
        Label(20 + i * 10, x, y, fill='dimGrey', size=14, bold=True)

drawThermostatLabels()

def onMouseDrag(mouseX, mouseY):
    # When the angle from the center of the thermostat knob to the mouse is
    # between 240 and 360 or between 0 and 120, move the thermostatLine to point
    # in that direction.
    angle=angleTo(200,225,mouseX,mouseY)
    if 0<angle<120 or 240<angle<360:
        x, y = getPointInDir(thermostatLine.x1, thermostatLine.y1, angle, 75)
        thermostatLine.x2=x
        thermostatLine.y2=y
    pass
