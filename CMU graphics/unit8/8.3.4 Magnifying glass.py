dotGrid = Group()

# Create an evenly spaced 9x9 grid of dots.
### (HINT: Use nested for loops to create the grid.)
for i in range(9):
    for y in range(9):
        dotGrid.add(
            Circle(40+40*i,40+40*y,5)
            )

# magnifying glass
just_glass = Circle(200, 200, 50, fill=gradient('white', 'steelBlue', start='left'),
           opacity=25)
magnifyingGlass = Group(
    just_glass,
    Circle(200, 200, 50, fill=None, border='silver'),
    Line(200, 250, 200, 300, lineWidth=10)
    )
magnifyingGlass.glassX = 200
magnifyingGlass.glassY = 200

def onMouseMove(mouseX, mouseY):
    magnifyingGlass.centerX = mouseX
    magnifyingGlass.centerY = mouseY
    magnifyingGlass.glassX = magnifyingGlass.centerX
    magnifyingGlass.glassY = magnifyingGlass.centerY - 25

    # Resize any dots who's centers are inside the glass.
    ### (HINT: Use a function learned in this Unit!)
    for dot in dotGrid:
        if just_glass.contains(dot.centerX, dot.centerY):
            dot.radius = 15
        else:
            dot.radius = 5
