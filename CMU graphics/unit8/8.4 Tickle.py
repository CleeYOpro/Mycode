app.background = 'black'

t = Label('tickle', 200, 200, fill='cyan', size=50)
fadedTickles = Group()

def onMouseMove(mouseX, mouseY):
    # If the mouse moves over the tickle label, add a new tickle label to the
    # group. Also change the original label's center to a new random position!
    ### (HINT: The tickle can move up to 10 pixels horizontally and up to 10
    #          pixels vertically (both inclusive).)
    if t.contains(mouseX,mouseY):
        fadedTickles.add(Label('tickle', t.centerX, t.centerY, fill='cyan',size=50))
        t.centerX+=randrange(-10,10)
        t.centerY+=randrange(-10,10)
    pass

def onStep():
    # Loop through each tickle label in the group and reduce opacity by 20.
    # If the opacity of the label is equal to 0, remove it from the group.
    for label in fadedTickles:
        if label.opacity>0:
            label.opacity-=20
        if label.opacity==0:
            fadedTickles.remove(label)
    pass
