app.background = 'whiteSmoke'

volume = Star(200, 210, 100, 10, fill='gold', opacity=30)
Rect(100, 85, 200, 50, fill=None, border='dimGray', borderWidth=10)
radio = Rect(30, 120, 335, 200, fill='indianRed')
radio.switchedOn = False

Rect(60, 185, 90, 100, fill='fireBrick')
Rect(250, 185, 90, 100, fill='fireBrick')
Rect(175, 185, 50, 100, fill='fireBrick')
Rect(100, 135, 200, 30, fill='gainsboro', border='dimGray')
Circle(105, 235, 35, fill='gray', border=rgb(60, 60, 60))
Circle(295, 235, 35, fill='gray', border=rgb(60, 60, 60))

# buttons
powerButton = Circle(80, 150, 10, fill='fireBrick')
topButton = Rect(190, 205, 20, 20, fill=rgb(45, 45, 45), border='grey',
                 borderWidth=1)
bottomButton = Rect(190, 245, 20, 20, fill=rgb(45, 45, 45), border='grey',
                    borderWidth=1)

songType = Label('', 200, 150, size=15)
powerButton.valu=0

def onMousePress(mouseX, mouseY):
    # Code the behavior in the solution canvas.
    ### (HINT: We've defined a few global variables, and one custom property
    #          thatz will be useful.)
    if powerButton.valu==0:
        powerButton.fill='mediumAquamarine'
    if powerButton.valu >=1:
        if topButton.hits(mouseX,mouseY):
            volume.radius=200
            songType.value='Quiet Piano'
        if bottomButton.hits(mouseX,mouseY):
            volume.radius=240
            songType.value='Loud rock'
    powerButton.valu+=1
    pass
