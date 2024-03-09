app.background = 'darkGrey'
app.stepsPerSecond = 20

bigRain = Group()
smallRain = Group()

cloud1 = Group()
cloud2 = Group()
cloud3 = Group()

def drawClouds():
    # Fill in the range for each of the for loops to draw the circles that make up
    # the clouds.
    ### Fix Your Code Here ###
    for i in range(6):
        cloud1.add(
            Circle(i * 60 + 60, 60, 55, fill='white', border='gainsboro')
            )
    cloud1.add(Oval(150, 60, 360, 80, fill='white'))

    for i in range(4):
        cloud2.add(
            Circle(i * 40 + 390, 50, 45, fill='snow', border='gainsboro')
            )
    cloud2.add(Oval(430, 50, 150, 70, fill='snow'))

    for i in range(5):
        cloud3.add(
            Circle(i * 60 + 590, 60, 65, fill='whiteSmoke', border='gainsboro')
            )
    cloud3.add(Oval(710, 60, 340, 90, fill='whiteSmoke'))

drawClouds()

# window
Rect(0, 0, 400, 400, fill=None, border='moccasin', borderWidth=30)
Rect(30, 30, 340, 340, fill=None, border='saddleBrown', borderWidth=20)
Line(200, 40, 200, 360, fill='saddleBrown', lineWidth=5)
Line(40, 200, 360, 200, fill='saddleBrown', lineWidth=5)
Rect(35, 35, 330, 330, fill=None, border='maroon', borderWidth=4)
Line(15, 375, 385, 375, fill='burlyWood', lineWidth=12)
Line(20, 385, 380, 385, fill='tan', lineWidth=8)

def drawRain():
    # Draw a single horizontal row of rain drops. Each drop of rain contains a
    # big rain drop, and a small rain drop that has lower opacity and lineWidth.
    for i in range(12):
        smallRain.add(
            Line(66+i*25,50,56+i*25,70, fill = 'lightBlue', lineWidth = 1, opacity = 75)
            )
        bigRain.add(
            Line(65+i*25,80,55+i*25,100, fill= 'lightBlue', lineWidth = 2)
            )
        
        ### (HINT: Use the inspector and count the drops horizontally to    
        #          determine the range of the loop. The y-position of each
        #          drop starts at 100 for the big drops and at 70 for the
        #          smaller drops. The x-position depends on i.)
        ### (HINT: We've already defined some groups for you at the top of
        #          the code.)
        
        pass

def onStep():
    drawRain()

    # Moves the rain groups and clears all rain if it gets to the bottom.
    bigRain.centerY += 20
    smallRain.centerY += 20
    if (bigRain.bottom > 400):
        bigRain.clear()
    if (smallRain.bottom > 400):
        smallRain.clear()

    # Moves the clouds so that they wraparound.
    cloud1.centerX -= 2
    cloud2.centerX -= 2
    cloud3.centerX -= 2
    if (cloud1.centerX <= -230):
        cloud1.centerX = 630
    if (cloud2.centerX <= -230):
        cloud2.centerX = 630
    if (cloud3.centerX <= -230):
        cloud3.centerX = 630
