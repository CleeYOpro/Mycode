# table
app.background = rgb(135, 105, 85)
Line(0, 200, 400, 200, fill=rgb(165, 125, 100), lineWidth=400, dashes=(40, 3))

# plate
Rect(120, 120, 550, 550, fill='white', border='skyBlue',
     borderWidth=10, rotateAngle=45)

# pancake
Circle(370, 315, 120, fill=rgb(240, 170, 90), border='navajoWhite', borderWidth=15)
Star(370, 315, 75, 7, fill='saddleBrown', roundness=85, rotateAngle=10, opacity=55)
Circle(360, 300, 10, fill='cornflowerBlue')
Star(360, 300, 7, 5, fill='royalBlue')
Circle(395, 310, 10, fill='cornflowerBlue')
Star(395, 310, 7, 5, fill='royalBlue')
Circle(370, 330, 10, fill='cornflowerBlue')
Star(370, 330, 7, 5, fill='royalBlue')

# fruits
Circle(290, 185, 20, fill='khaki')
Star(290, 185, 16, 3, fill='orange', opacity=40, roundness=20)
Circle(380, 175, 20, fill='khaki')
Star(380, 175, 16, 3, fill='orange', opacity=40, roundness=20)
Circle(365, 110, 45, fill='lightYellow', border='darkOrange', borderWidth=3)
Circle(365, 110, 36, fill=rgb(255, 100, 70))
Star(365, 110, 30, 8, fill='lightYellow', roundness=8, rotateAngle=15)
Circle(235, 220, 30, fill='yellowGreen', border='peru', borderWidth=5)
Star(235, 220, 20, 20, fill=None, border='dimGrey', dashes=(1, 3))
Star(235, 220, 11, 15, fill='cornSilk', roundness=80)

def drawOrangeJuice(x, y):
    Circle(x, y, 50, fill='lightBlue')
    Circle(x, y, 45, fill=gradient('gold', 'darkOrange'), opacity=65)
    Rect(x + 35, y - 35, 10, 40, fill='darkOrange', rotateAngle=60)

def drawBacon(x, y):
    Line(x, y - 10, x + 90, y + 110, fill='maroon', lineWidth=40,
         dashes=(18, 12))
    Line(x + 10, y, x + 90, y + 100, fill='maroon', lineWidth=40,
         dashes=(18, 12))
    Line(x, y - 10, x + 90, y + 110, fill='navajoWhite', lineWidth=10,
         dashes=(18, 12))
    Line(x + 10, y, x + 90, y + 100, fill='navajoWhite', lineWidth=10,  
         dashes=(18, 12))

def onMousePress(mouseX, mouseY):
    # Draw a slice of bacon if we click on the plate. Otherwise, draw a glass
    # of orange juice.
    ### (HINT: Your condition is going to need to use the values mouseX, mouseY,
    #          and 400.)
    if mouseX<400-mouseY:
        drawOrangeJuice(mouseX, mouseY)
    if mouseX>400-mouseY:
        drawBacon(mouseX, mouseY)
    pass
