app.background = 'black'
app.rippleSpace = 40

ripples = Group()

def drawRipples():
    ripples.clear()
    for i in range(20,200,app.rippleSpace):
        ripples.add(Circle(200,200,i,fill= None, border = gradient('red', 'orange', 'yellow', 'lawnGreen', start ='top')))
drawRipples()
    # Draw ripples from the middle of the canvas to the edges.
    # The distance between ripples is determined by app.rippleSpace.
    ### (HINT: The radius of the smallest circle should determine where
    #          you start the for loop. 200 should be the end-value
    #          in the for loop.)
    ### (HINT: Add each circle you draw to the ripples group.)
    

def onKeyHold(keys):
    if ('up' in keys):
        app.rippleSpace += 2
    elif (('down' in keys) and (app.rippleSpace > 2)):
        app.rippleSpace -= 2
    drawRipples()
