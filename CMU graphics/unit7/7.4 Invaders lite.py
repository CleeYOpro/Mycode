app.background = 'black'
app.stepsPerSecond = 15

Label('Invaders Lite', 200, 20, fill='white', size=20, bold=True)
Label('left and right move the ship', 200, 40, fill='white')
Label('all other keys launch the laser', 200, 55, fill='white')

score = Label(0, 325, 40, fill='white', size=40, bold=True)
player = Polygon(200, 355, 199, 360, 195, 365, 195, 365, 187, 370, 180, 380,
                 193, 373, 197, 373, 200, 380, 203, 373, 207, 373,
                 220, 380, 213, 370, 205, 365, 205, 365, 201, 360,
                 fill=gradient('lavender', 'thistle', 'fuchsia', start='top'))
player.dx = 10

laser = Circle(player.centerX, player.top, 5, fill='lime', visible=False,
               align='bottom')
laser.dy = -15

invaders = Group()
invaders.dx = 8
invaders.dy = 8
invaders.number = 0

def addInvadersRow(centerY, color):
    # Creates a row of invaders.
    for i in range(5):
        centerX = 100 + 50 * i
        invader = Group(
            RegularPolygon(centerX, centerY - 2, 8, 3, fill=color),
            Rect(centerX - 3, centerY - 10, 6, 5),
            Line(centerX - 3, centerY - 1, centerX + 3, centerY - 1,
                 dashes=(2, 2)),
            Line(centerX - 7, centerY + 3, centerX + 7, centerY + 3, fill=color,
                 dashes=(2, 1))
            )

        invaders.add(invader)
        invaders.number += 1

def addInvaders():
    # Creates all of the invaders for that wave.
    addInvadersRow(100, 'red')
    addInvadersRow(130, 'cyan')
    addInvadersRow(160, 'yellow')

addInvaders()

def gameOver():
    Label('Game Over', 200, 200, fill='white', size=50, bold=True)
    app.stop()

def speedUpInvaders():
    # Every time a wave is cleared, speeds the next wave up.
    if (invaders.dx < 0):
        invaders.dx -= 2
    else:
        invaders.dx += 2
    invaders.dy += 1

def removeHitInvaders():
    # For each invader, if the projectile hits that invader, remove
    # it from the group of invaders and add one to the score.
    ### Place Your Code Here ###
    for i in invaders.children:
        if laser.hitsShape(i):
            invaders.remove(i)
            score.value +=1
    # If there are no more invaders, get new ones using addInvaders, and
    # speed them up using speedUpInvaders.
        if len(invaders) == 0:
            addInvaders()
            speedUpInvaders()
    pass

def moveDotUp():
    # Moves the laser up by laser.dy, and hides it if it is too high.
    # Otherwise removes any invaders that got hit.
    laser.centerY += laser.dy
    if (laser.centerY <= 75):
        laser.visible = False
    else:
        removeHitInvaders()

def moveInvaders():
    # Moves all the invaders one step left or right.
    invaders.centerX += invaders.dx

    # If it hits the edge, reverse direction and move down a bit.
    if ((invaders.left <= 0) or (invaders.right >= 400)):
        invaders.dx = -invaders.dx
        invaders.centerY += invaders.dy

def testInvaders(x, y):
    ### This function is for testing purposes only. DO NOT edit this function.
    # Removes all invaders, adds a new one, and places the player right under it.
    invaders.clear()
    invaders.add(
        Circle(x, y, 10, fill='orange')
        )
    invaders.number = 1
    player.centerX = x

def onKeyPress(key):
    # Fires a laser.
    if ((key != 'left') and (key != 'right')):
        laser.centerX = player.centerX
        laser.bottom = player.top
        laser.visible = True

def onKeyHold(keys):
    # When the left arrow is pressed, move the player by its dx and bound it
    # by the left edge of the canvas.
    if 'left' in keys and player.left > 0:
        player.centerX-=10

    # When the right arrow is pressed, move the player by its dx and bound it
    # by the right edge of the canvas.
    if 'right' in keys and player.right <400:
        player.centerX+=10
    pass

def onStep():
    # First moves the invaders.
    moveInvaders()

    # Next, checks if we lost the game.
    if (invaders.bottom > player.top):
        gameOver()

    # Then, moves the projectile if it's visible.
    if (laser.visible == True):
        moveDotUp()
