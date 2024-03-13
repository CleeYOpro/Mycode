app.background = 'black'

app.steps = 0

asteroids = Group()

earth = Circle(200, 200, 50, fill=gradient('blue', 'green', start='left-top'))

def createAsteroid():
    angle = randrange(0, 360)
    cx, cy = getPointInDir(200, 200, angle, 180)
    asteroid = Circle(cx, cy, 6, fill=rgb(180, 110, 40))
    asteroid.dx = randrange(-5, 6)
    asteroid.dy = randrange(-5, 6)
    asteroids.add(asteroid)

def onStep():
    for asteroid in asteroids:
        # Moves the asteroid.
        asteroid.centerX += asteroid.dx
        asteroid.centerY += asteroid.dy

        # Removes the asteroid if it hits the earth or leaves the canvas.
        if (asteroid.hitsShape(earth) == True):
            asteroids.remove(asteroid)
        if (((asteroid.right < 0) and (asteroid.dx < 0)) or
            ((asteroid.left > 400) and (asteroid.dx > 0)) or
            ((asteroid.bottom < 0) and (asteroid.dy < 0)) or
            ((asteroid.top > 400) and (asteroid.dy > 0))):
            asteroids.remove(asteroid)

        # Get a point that is 0.1 pixels from the asteroid, in the direction of
        # the earth.
        curve=angleTo(earth.centerX, earth.centerY, asteroid.centerX, asteroid.centerY)
        x,y=getPointInDir(asteroid.centerX,asteroid.centerY,curve,0.1)
        # Add the difference between the x-coordinate of that point and the
        # asteroid's current centerX to the asteroid's dx property.
        # Do the same for the asteroid's dy property.
        asteroid.dx+=(asteroid.centerX-x)
        asteroid.dy+=(asteroid.centerY-y)
    # Creates a new asteroid every second.
    app.steps += 1
    if (app.steps % 30 == 0):
        createAsteroid()
