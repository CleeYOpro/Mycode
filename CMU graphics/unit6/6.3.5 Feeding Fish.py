app.background = gradient('cyan', 'deepSkyBlue', 'royalBlue', start='top')

# Run faster than the default.
app.stepsPerSecond = 60

# food
food = Circle(275, 0, 5, fill='orange')
Label('Food eaten:', 200, 345, fill='white', size=25)
foodCount = Label(0, 200, 375, fill='white', size=25)

# fish
fishBody = Oval(100, 200, 60, 40, fill=gradient('lightSteelBlue', 'yellow', start='left'))
fishTail = Polygon(70, 200, 60, 180, 60, 220,
                   fill=gradient('gold', 'yellow', start='left'))
fishEye = Circle(115, 195, 2)
fish = Group(fishBody, fishTail, fishEye)

# Start the fish right in the center of the canvas.
fish.centerX = 200
fish.centerY = 300

def onStep():
    # Move the fish horizontally by 5 pixels and the food vertically by 2 pixels.
    # Don't forget to wraparound!
    ### (HINT: Wrap the food using its centerY, not its top or bottom!)
    ### Place Your Code Here ###
    fish.centerX+=5
    food.centerY+=2
    if(fish.hitsShape(food)==True):
        food.centerY=0
        fish.width+=5
        fish.height+=5
        foodCount.value+=1
    # If the fish eats the food, put it at the top again and increase the fish
    # size by 5 pixels. Otherwise, move the fish up or down 1 pixel towards
    # the food.
    if food.centerY>fish.centerY:
        if fish.centerY<=399:
            fish.centerY+=1
    if fish.left>400:
        fish.right=0
    if food.centerY>400:
        food.centerY=0
    if food.centerY<fish.centerY:
        if fish.centerY>=1:
            fish.centerY-=1
    ### Place Your Code Here ###
    pass
