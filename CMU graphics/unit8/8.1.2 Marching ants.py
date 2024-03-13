app.background = 'forestGreen'

app.steps = 0
app.prevAntDir = 0

Circle(0, 200, 100, fill=gradient('peru', 'sienna'))
Circle(0, 200, 20, fill=rgb(80, 40, 40))

ants = Group()

def createAnt():
    ant = Circle(0, 200, 5)
    ant.dx = 5
    ant.dy = 0
    ant.upOrDown = (app.prevAntDir + 1) % 2
    app.prevAntDir = ant.upOrDown
    ants.add(ant)

def onStep():
    # Every 10 steps, create a new ant.
    if app.steps %10==0:
        createAnt()

    for ant in ants:
        ant.centerX += ant.dx
        ant.centerY += ant.dy

        if (ant.centerX > 400):
            ants.remove(ant)
        elif (ant.centerX > 150):
            ant.dx = 3.5

            # Depending on if the ant should move up or down, set the
            # ant's dy property to 2 or -2.
            ### (HINT: Each ant has an upOrDown property that is defined in
            #          the createAnt function above.)
            if ant.upOrDown %  2==0:
                ant.dy = 2
            else:
                ant.dy =-2

    app.steps += 1
