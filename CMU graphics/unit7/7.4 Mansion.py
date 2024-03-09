app.background = 'lightSkyBlue'

# trees
Circle(10, 227, 10, fill='forestGreen')
Circle(23, 221, 8, fill='forestGreen')
Circle(34, 234, 12, fill='forestGreen')
Circle(45, 233, 7, fill='forestGreen')
Circle(11, 252, 30, fill='forestGreen')
Circle(41, 260, 25, fill='forestGreen')
Circle(351, 227, 10, fill='forestGreen')
Circle(370, 221, 8, fill='forestGreen')
Circle(400, 234, 12, fill='forestGreen')
Circle(380, 225, 7, fill='forestGreen')
Circle(370, 249, 30, fill='forestGreen')
Circle(390, 260, 25, fill='forestGreen')

# mansion
Rect(50, 200, 300, 105, fill='white', border='lightGrey', borderWidth=3)
Rect(100, 150, 200, 155,  fill='white', border='lightGrey', borderWidth=3)
Polygon(50, 205, 105, 205, 75, 180, fill='lightGrey')
Polygon(295, 203, 350, 203, 325, 180, fill='lightGrey')
Polygon(100, 155, 200, 90, 300, 155, fill='lightGrey')
Polygon(200, 60, 225, 60, 220, 70, 230, 80, 200, 75, fill='brown')
Line(200, 90, 200, 60, fill='grey')

def drawSquareWindow(cx, cy):
    window = Group(
        Rect(185, 180, 30, 40, fill='lightCyan', border='lightGrey'),
        Line(200, 190, 200, 210, fill='lightGrey', lineWidth=30, dashes=(2, 14)),
        Line(200, 180, 200, 220, fill='lightGrey')
        )
    window.centerX = cx
    window.centerY = cy

drawSquareWindow(135, 200)
drawSquareWindow(265, 200)
drawSquareWindow(75, 250)
drawSquareWindow(135, 250)
drawSquareWindow(265, 250)
drawSquareWindow(325, 250)

# circle windows
Arc(200, 225, 40, 40, 270, 180, fill='lightCyan', border='lightGrey')
Line(200, 220, 200, 205, fill='lightGrey')
Line(200, 220, 185, 210, fill='lightGrey')
Line(200, 220, 215, 210, fill='lightGrey')
Arc(135, 182, 30, 30, 270, 180, fill='lightCyan', border='lightGrey')
Line(135, 170, 135, 200, fill='lightGrey')
Line(135, 182, 125, 170, fill='lightGrey', lineWidth=1.5)
Line(135, 182, 145, 170, fill='lightGrey', lineWidth=1.5)
Arc(265, 182, 30, 30, 270, 180, fill='lightCyan', border='lightGrey')
Line(265, 170, 265, 200, fill='lightGrey')
Line(265, 182, 255, 170, fill='lightGrey', lineWidth=1.5)
Line(265, 182, 275, 170, fill='lightGrey', lineWidth=1.5)
Oval(200, 180, 40, 30, fill='lightCyan', border='lightGrey')

# entryway
Rect(180, 220, 40, 50, fill='darkGrey', border='grey')
Line(200, 260, 200, 220, fill='grey')
Polygon(150, 305, 180, 260, 220, 260, 250, 305, fill='lightGrey')

# bushes
Circle(5, 290, 20, fill='lightGreen')
Circle(25, 275, 10, fill='lightGreen')
Circle(40, 290, 20, fill='lightGreen')
Circle(60, 295, 15, fill='lightGreen')
Circle(85, 290, 15, fill='lightGreen')
Circle(105, 280, 5, fill='lightGreen')
Circle(115, 275, 5, fill='lightGreen')
Circle(130, 280, 10, fill='lightGreen')
Circle(120, 295, 25, fill='lightGreen')
Circle(145, 295, 5, fill='lightGreen')
Circle(260, 295, 10, fill='lightGreen')
Circle(280, 290, 20, fill='lightGreen')
Circle(295, 275, 10, fill='lightGreen')
Circle(310, 290, 20, fill='lightGreen')
Circle(330, 290, 15, fill='lightGreen')
Circle(350, 285, 15, fill='lightGreen')
Circle(365, 280, 5, fill='lightGreen')
Circle(375, 280, 5, fill='lightGreen')
Circle(385, 280, 10, fill='lightGreen')
Circle(360, 300, 25, fill='lightGreen')
Circle(390, 295, 20, fill='lightGreen')

# lawn
Rect(0, 300, 400, 100, fill='oliveDrab')

def drawFence():
    isHighBar = True

    # Draw all 45 fence posts. Use the isHighBar variable to alternate between
    # tall and short posts. Each post is composed of two lines, one of which uses
    # an arrow.
    for i in range(45):
        if isHighBar == True:
            Line(i*10, 265, i*10, 400, lineWidth = 1.5)
            Line(i*10, 250, i*10, 265, arrowStart=True,lineWidth = 1.5,  fill = 'goldenRod')
            isHighBar = False
        else:
            Line(10+(i*20), 275, 10+(i*20), 400, lineWidth = 1.5)
            Line(10+((i-1)*20), 275, 10+((i-1)*20), 400, lineWidth = 1.5)
            
            Line(10+(i*20), 260, 10+(i*20), 275, arrowStart=True, lineWidth = 1.5,  fill = 'goldenRod')
            Line(10+((i-1)*20), 260, 10+((i-1)*20), 275, arrowStart=True, lineWidth = 1.5, fill = 'goldenRod')
            isHighBar = True
    

drawFence()

Line(0, 285, 400, 285)
Line(0, 350, 400, 350)
Rect(0, 370, 400, 30, fill='lightGrey')
Line(0, 370, 400, 370, fill='slateGray', lineWidth=5)
