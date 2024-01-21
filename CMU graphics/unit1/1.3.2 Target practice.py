# Draws the background.
Rect(0, 0, 400, 400, fill='ghostWhite')

# Draw the rope that the target hangs from.
### (HINT: This exercise requires some careful use of the Inspector!)
### Place Your Code Here ###
Line(0,0,200,225, fill='dimGrey', lineWidth=6, dashes=True)
Line(400,0,200,225, fill='dimGrey', lineWidth=6, dashes=True)
# Now draw the target.
### Place Your Code Here ###
Circle(200,225,150, fill='dodgerBlue', border='black')
Circle(200,225,100, fill='crimson', border='black', borderWidth=1)
Circle(200,225,45, fill='yellow', border='black', borderWidth=1)
