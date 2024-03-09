app.background = rgb(105, 140, 35)
app.stepsPerSecond = 2.5

def drawVeggie(x,y):
    v = Group(
        Line(115, 235, 123, 245, fill='forestGreen', lineWidth=5),
        Line(120, 235, 128, 245, fill='forestGreen', lineWidth=5)
        )
    v.centerX = x
    v.centerY = y

def drawPizza():
    # pizza
    Arc(210, 310, 300, 300, 270, 60, fill=rgb(140, 70, 20))
    Arc(210, 310, 280, 280, 270, 60, fill=rgb(250, 190, 80))
    Arc(210, 310, 280, 280, 270, 30, fill=rgb(255, 230, 180))

    # pepperoni
    Circle(160, 280, 10, fill=rgb(205, 50, 50))
    Circle(160, 250, 10, fill=rgb(205, 50, 50))
    Circle(130, 290, 10, fill=rgb(205, 50, 50))
    Circle(95, 295, 10, fill=rgb(205, 50, 50))
    Circle(135, 225, 10, fill=rgb(205, 50, 50))

    drawVeggie(115, 235)
    drawVeggie(150, 270)
    drawVeggie(145, 220)
    drawVeggie(95, 275)

drawPizza()

bite1 = Circle(225, 305, 5, fill=rgb(105, 140, 35))
bite2 = Circle(180, 355, 5, fill=rgb(105, 140, 35))

# face
Circle(350, 230, 150, fill=rgb(140, 70, 20))
Oval(380, 400, 120, 220, fill=rgb(140, 70, 20), rotateAngle=-30)
eye = Line(250, 205, 285, 205, lineWidth=5)

mouth = Arc(305, 270, 200, 200, 230, 40, fill=rgb(105, 140, 35))

# hat
Polygon(230, 125, 470, 125, 420, 25, 280, 25, fill=rgb(210, 180, 140))
Polygon(235, 115, 230, 125, 470, 125, 465, 115, fill='white')
Polygon(230, 125, 225, 115, 218, 118, 225, 135, 475, 135, 482, 118, 475, 115,
        470, 125)
Line(245, 95, 400, 95, lineWidth=10, dashes=True)

def onStep():
    # As long as the bites don't cover the pizza, move the mouth. Also, increase
    # both of the bites' radii when the person bites down.
    if bite1.radius <=155:
        if mouth.startAngle == 230:
            mouth.startAngle = 240
            mouth.sweepAngle = 20
            bite1.radius+=25
            bite2.radius+=25
        else:
            mouth.startAngle = 230
            mouth.sweepAngle = 40
        
        
    pass
