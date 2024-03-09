app.background = 'black'

waves = Group()
waves.maxSize = 300
waves.minSize = 10
waves.stepSize = 10

def makePattern():
    for i in range(25):
        # Color 1 should have a blue rgb value of i * 10,
        # color 2 should have a red rgb value of i * 10, and all other
        # parts of the rgbs should be 0.
        
        color1 = rgb(0, 0, i*10)
        color2 = rgb(i*10, 0, 0)

        # Add a new circle to the pattern group.
        waves.add(
            Circle(200, 200, (i + 1) * 10, fill=None,
                   border=gradient(color1, color2, start='top'), borderWidth=12)
            )

makePattern()

def onStep():
    # For each wave when the current circle is bigger than or equal to
    # the maximum size, reset the radius to the minimum size.
    # Otherwise, increase the radius by the stepSize.
    for circle in waves.children:
        if circle.radius >= waves.maxSize:
            circle.radius = waves.minSize
        else:
            circle.radius += waves.stepSize
    pass
