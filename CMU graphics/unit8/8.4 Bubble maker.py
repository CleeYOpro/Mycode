app.background = 'black'

Line(200, 400, 200, 300, fill=gradient('silver', 'dimGrey', start='left'),
     lineWidth=40)
Oval(200, 300, 40, 10, fill='dimGrey')

color = 'dodgerBlue'
bubbles = Group()

def onStep():
    for bubble in bubbles:
        # Move the bubble horizontally a random distance between -10 and 10 pixels.
        bubble.centerX+=randrange(-10,11)
        
        # Moves the bubble up and removes it when it becomes too transparent.
        bubble.centerY -= 5
        bubble.opacity -= 2
        if (bubble.opacity <= 1):
            bubbles.remove(bubble)

    # Add a new bubble every step.
    bubbles.add(
        Circle(200, 290, 15, fill=color)
        )
