app.background = gradient(rgb(135, 250, 250), rgb(15, 125, 195), start='top')

# fish
yellowFish = Polygon(140, 100, 100, 60, 110, 95, 90, 85, 100, 100, 90, 120,
                     110, 105, 100, 140,
                     fill=gradient('white', 'lemonChiffon', 'gold', 'darkOrange',
                                   start='right'))
yellowFishEye = Circle(130, 95, 3)
yl = Label(0, 50, 100, fill='yellow', size=50)

purpleFish = Polygon(140, 300, 100, 260, 110, 295, 90, 285, 100, 300, 90, 320,
                     110, 305, 100, 340,
                     fill=gradient('white', 'lavender', 'orchid', 'darkOrchid',
                                   start='right'))
purpleFishEye = Circle(130, 295, 3)
pl = Label(0, 50, 300, fill=rgb(210, 190, 255), size=50)

Label('Underwater Tag', 200, 20, size=22)
Label('When two fish collide, the fish on the left scores that point.', 200, 40)
Label('One fish moves faster up/down, the other moves faster left/right!', 200, 55)

def checkFishIntersection():
    # Check if the fish intersect and add a point for the fish that is further left.
    ### (HINT: What happens when the fish have the same x-coordinate?
    #          Play with the canvas or test cases to figure it out!)
    ### Place Your Code Here ###
    if yellowFish.hitsShape(purpleFish):
        if yellowFish.centerX < purpleFish.centerX:
            yl.value += 1
        else:
            pl.value+=1
        yellowFish.centerX = 115
        yellowFish.centerY = 100
        yellowFishEye.centerX = 130
        yellowFishEye.centerY = 95
        
        purpleFish.centerX = 115
        purpleFish.centerY = 300
        purpleFishEye.centerX = 130
        purpleFishEye.centerY = 295
    # This code resets the fish to their original locations. This should happen
    # only if the fish intersect.
    ### Fix Your Code Here ###



def checkFishWraparound(fish):
    # Check if a fish is outside the canvas bounds and wraparound. Use the
    # left, right, top, and bottom for wrapping, not centerX and centerY.
    ### Place Your Code Here ###
    if purpleFish.right < 0:
        purpleFish.left = 400
    if purpleFish.left >400:
        purpleFish.right = 0
    if yellowFish.right < 0:
        yellowFish.left = 400
    if yellowFish.left  > 400:
        yellowFish.right = 0
        
    if purpleFish.bottom < 0:
        purpleFish.top = 400
    if purpleFish.top >400:
        purpleFish.bottom = 0
    if yellowFish.bottom < 0:
        yellowFish.top = 400
    if yellowFish.top  > 400:
        yellowFish.bottom = 0
    pass

def moveEyes():
    # Moves the eyes of both fish relative to its body.
    yellowFishEye.centerX = yellowFish.centerX + 15
    yellowFishEye.centerY = yellowFish.centerY - 5
    purpleFishEye.centerX = purpleFish.centerX + 15
    purpleFishEye.centerY = purpleFish.centerY - 5

def onKeyHold(keys):
    # Move the fish in their respective directions.
    if ('w' in keys):
        yellowFish.centerY -= 10
    elif ('s' in keys):
        yellowFish.centerY += 10
    elif ('a' in keys):
        yellowFish.centerX -= 5
    elif ('d' in keys):
        yellowFish.centerX += 5

    if ('up' in keys):
        purpleFish.centerY -= 5
    elif ('down' in keys):
        purpleFish.centerY += 5
    elif ('left' in keys):
        purpleFish.centerX -= 10
    elif ('right' in keys):
        purpleFish.centerX += 10

    checkFishWraparound(yellowFish)
    checkFishWraparound(purpleFish)

    # Move the eyes.
    moveEyes()

    # Update score appropriately, if fish intersect each other.
    checkFishIntersection()
