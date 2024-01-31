app.background = 'fireBrick'

# eye
Oval(200, 200, 300, 200, fill=gradient('darkGoldenrod', 'olive'), border='black',
     borderWidth=3)
Star(200, 200, 100, 200, fill=gradient('orange', 'gold'), opacity=70)
Polygon(200, 110, 170, 155, 170, 245, 200, 290, 230, 245, 230, 155)
Oval(200, 200, 79, 140)

eyelid = Oval(225, 50, 360, 210, fill='fireBrick')

sleepLabel = Label('Zzz...', 300, 60, size=40, font='monospace', visible=False)

def onMouseMove(mouseX, mouseY):
    # Move the eyelid with the mouse and display the sleeping label if the mouse
    # is in the lower half of the canvas.
    if (mouseY<200):
        eyelid.centerY=mouseY
    
    if (mouseY<200):
        sleepLabel.visible=False
    else: 
        sleepLabel.visible=True
    pass
