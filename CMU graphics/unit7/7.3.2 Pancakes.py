app.background = 'lavender'

Rect(0, 250, 400, 150, fill='sienna')
Oval(200, 370, 340, 50, opacity=30)
Oval(200, 360, 350, 50, fill='ghostWhite')
Oval(200, 360, 336, 45, fill=None, border='steelBlue', borderWidth=1, opacity=60)
Oval(200, 360, 300, 25, opacity=6)
Oval(200, 360, 315, 35, opacity=4)
Oval(200, 360, 315, 35, fill=None, border='black', borderWidth=1, opacity=10)

def drawPancake(cy):
    Rect(200, cy + 5, 250, 10, fill='wheat', align='center')
    Oval(200, cy + 10, 250, 20, fill='wheat')
    Oval(200, cy, 250, 20, fill='tan')

def drawPancakes(numCakes):
    # Draw a stack of pancakes with numCakes pancakes in it.
    # Each pancake should be drawn 15 pixels above the one below it.

    for i in range(numCakes):
        drawPancake(350-15*i)

##### Place your code above this line, code below is for testing purposes #####
# test case:
drawPancakes(10)
