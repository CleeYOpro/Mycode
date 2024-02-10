app.background = 'seaGreen'

# eyes
Oval(110, 120, 70, 120, fill='white')
Oval(290, 120, 70, 120, fill='white')
Oval(110, 120, 50, 80, fill=gradient('skyBlue', 'skyBlue', 'blue'))
Oval(290, 120, 50, 80, fill=gradient('skyBlue', 'skyBlue', 'blue'))
Oval(110, 120, 30, 50)
Oval(290, 120, 30, 50)

mouth = Oval(200, 320, 40, 5, fill='pink', border='black', borderWidth=4)

def expandHorizontal():
    mouth.width += 2

def expandVertical():
    mouth.height += 2

def onKeyHold(keys):
    # Expand based on the keys held.
    ### (HINT: Use compound conditionals to check that both arrow keys
    #          are being pressed and use the helper functions.)
    if 'up' in keys and 'down' in keys:
        expandVertical()
    if 'left' in keys and 'right' in keys:
        expandHorizontal()
    pass
