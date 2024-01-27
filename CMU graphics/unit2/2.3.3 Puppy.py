# background
app.background = 'wheat'

# head
Oval(200, 200, 250, 210, fill='saddleBrown')
Oval(200, 255, 150, 107, fill='saddleBrown', border='black')
Circle(200, 270, 55, fill='saddleBrown')

# tongue
tongue = Oval(200, 310, 70, 100, fill='lightCoral', visible=False)

# face
Circle(165, 255, 40, fill='saddleBrown', border='black')
Circle(235, 255, 40, fill='saddleBrown', border='black')
Oval(200, 240, 130, 70, fill='saddleBrown')
Circle(200, 240, 30)
Polygon(200, 277, 190, 265, 210, 265)

# eyes
Circle(240, 170, 20)
Circle(235, 165, 7, fill='white')
Circle(245, 170, 3, fill='white')
Circle(160, 170, 20)
Circle(155, 165, 7, fill='white')
Circle(165, 170, 3, fill='white')

# ears
Oval(90, 160, 70, 150, rotateAngle=45)
Oval(310, 160, 70, 150, rotateAngle=-45)

def onMousePress(mouseX, mouseY):
    # Make the puppy's tongue show up.
    tongue.visible=True
    pass

def onMouseRelease(mouseX, mouseY):
    # Make the puppy's tongue disappear.
    tongue.visible=False
    pass