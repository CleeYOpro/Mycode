app.background = 'tan'

Polygon(180, 265, 145, 400, 255, 400, 220, 265, fill=rgb(160, 140, 110))
Oval(100, 180, 150, 225, fill='white')
Oval(300, 180, 150, 225, fill='white')

leftEye = Circle(140, 180, 30, fill=rgb(60, 60, 60))
rightEye = Circle(340, 180, 30, fill=rgb(60, 60, 60))

def onKeyPress(key):
    # When the left or right arrow key is pressed, move the irises to the
    # appropriate side of the eye.
    if key == 'left':
        leftEye.centerX = 60
        rightEye.centerX = 260
    if key == 'right':
        leftEye.centerX = 140
        rightEye.centerX = 340
    pass
