app.background = 'lightCyan'
app.stepsPerSecond = 20
app.steps = 0

ripples = Group()

def onStep():
    # Create a ripple with random x and y center, and add it to ripples group.
    ### Place Your Code Here ###
    x=randrange(0,400)
    y=randrange(0,400)
    ripples.add(Circle(x,y,5,fill= None, border = 'lightBlue', borderWidth = 20))
    # Goes through each ripple and makes the border decrease and the ripple expand.
    for ripple in ripples.children:
        ripple.borderWidth -= 2
        ripple.radius += 5

        # If the ripple fades out, remove it.
        if (ripple.borderWidth <= 0):
            ripples.remove(ripple)
