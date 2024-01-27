app.background = gradient('midnightBlue', 'dodgerBlue', start='top')

# Define the platform and ball variables.
### (HINT: You can't see the left-top of the platform so try to position it by
#          using a different alignment!)
### Fix Your Code Here ###
platform =Rect (-50,150,300,300,fill=gradient('grey', 'gainsboro', start='left-top'))
ball = Circle(100,platform.top-20, 20, fill='crimson')

def onMousePress(mouseX, mouseY):
    # Rotate the platform and bounce the ball.
    platform.rotateAngle-=10
    ball.bottom=platform.top
    pass