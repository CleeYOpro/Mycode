app.background = 'lightSlateGrey'

def drawScene():
    # Draws the basic shape of the table.
    Rect(50, 30, 350, 370, fill='tan')

    # The texture on the table is drawn using a bunch of vertical lines that have
    # random opacities between 0 and 30 (exclusive). Draw these lines.
    for i in range(100):
        opa =randrange(0,30)
        Line(50 + 4*i, 30 , 50 + 4*i, 400 ,opacity = opa, lineWidth = 4, fill = 'sienna')

    # Draws the tomato.
    Oval(345, 115, 150, 130, fill='crimson')
    Star(345, 115, 60, 13, fill='seaGreen', roundness=50)

    # Draws the knife.
    Oval(217, 180, 30, 230, fill='silver', rotateAngle=-15)
    Oval(235, 295, 30, 100, fill='silver')
    Polygon(185, 70, 165, 345, 235, 345, 240, 280, 220, 170, fill='darkGrey')
    Rect(165, 345, 50, 100, fill='sienna')
    Star(185, 65, 20, 12, fill='red', roundness=10)
    Star(185, 65, 20, 12, fill='gold', roundness=10, rotateAngle=10)
    Star(185, 65, 10, 12, fill='white', roundness=10, rotateAngle=5)

drawScene()
