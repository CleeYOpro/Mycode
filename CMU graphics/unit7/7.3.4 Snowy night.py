app.background = gradient('navy', 'midnightBlue', start='top')

# the two snow piles
snowPile1 = Circle(450, 500, 250, fill='ghostWhite')
snowPile2 = Circle(-100, 1000, 700, fill='snow')

lamp = Group(
    Line(275, 130, 275, 350, lineWidth=10),
    Oval(275, 85, 40, 50),
    Polygon(255, 130, 295, 130, 305, 125, 245, 125),
    Polygon(260, 125, 290, 125, 295, 90, 255, 90,
            fill=gradient('white', 'yellow', 'gold')),
    Polygon(240, 90, 310, 90, 305, 85, 245, 85)
    )

lampCover = Group(
    Rect(265, 350, 20, 300, fill='ghostWhite'),
    Polygon(270, 350, 280, 350, 270, 355),
    Oval(275, 352, 15, 4, fill='darkGrey', rotateAngle=-30)
    )

snowFlakes = Group()

def onMousePress(mouseX, mouseY):
    snowFlakes.add(
        Star(mouseX, mouseY, 8, 8, fill='white')
        )

def onStep():
    # Move each snowflake down by 5 pixels.
    for i in snowFlakes.children:
        i.centerY+=5

    # If it reaches either snow pile, increase that pile's radius by 5 pixels,
    # and remove the snowflake. Also, if it hits the right snow pile, move the
    # lampCover up by 2 pixels.
        if (i.hitsShape(snowPile2)):
            snowPile2.radius +=5    
            snowFlakes.remove(i)
        if (i.hitsShape(snowPile1)):
            snowPile1.radius +=5
            snowFlakes.remove(i)
            lampCover.centerY -= 2
        
    pass
