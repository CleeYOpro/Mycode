app.background = gradient('skyBlue', 'lightBlue', start='top')

o = Oval(200, 200, 200, 200, fill=gradient('lemonChiffon', 'gold'))

def onMouseMove(mouseX, mouseY):
    # Change the width and height of the oval based on mouse position.
    # Make sure there are no issues when mouseX or mouseY is 0!
    ### (HINT: Carefully use the Inspector to figure out how to update
    #          the width and height using mouseX and mouseY.)
    o.width=mouseX+1
    o.height=mouseY+1
    pass
