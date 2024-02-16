app.background = gradient('skyBlue', 'lightBlue', start='bottom')

Star(360, 40, 40, 500, fill='yellow')
Circle(300, 325, 150, fill=gradient('darkGreen', 'forestGreen', start='bottom'))
Oval(100, 400, 300, 350, fill=gradient('darkGreen', 'forestGreen', start='bottom'))

# clouds
cloud = Oval(100, 40, 100, 50, fill=gradient('whiteSmoke', 'white', start='bottom'),
             opacity=90)
Oval(65, 170, 40, 15, fill='white')
Circle(56, 166, 8, fill='white')
Circle(71, 167, 10, fill='white')

# windmills
Line(100, 250, 100, 150, fill=gradient('silver', 'whiteSmoke', start='left'),
     lineWidth=8)
Line(275, 200, 275, 100, fill=gradient('silver', 'whiteSmoke', start='left'),
     lineWidth=8)

turbine1 = Star(100, 150, 60, 3, fill=gradient('silver', 'whiteSmoke'),
                roundness=10, rotateAngle=10)
turbine2 = Star(275, 100, 60, 3, fill=gradient('silver', 'whiteSmoke'),
                roundness=10, rotateAngle=30)

def onStep():
    # Animate the windmills by adjusting the rotateAngle.
    ### (HINT: Try using the test cases to see how much to rotate the windmills!)
    turbine1.rotateAngle+=3
    turbine1.direction='clockwise'
    turbine2.rotateAngle+=2
    turbine2.direction='clockwise'

    # Move the cloud across the screen. If the cloud drifts offscreen, put it back
    # onscreen.
    cloud.centerX+=1
    if (cloud.left > 400):
        cloud.right = 0
    pass
