# Draws the table and the paper.
Rect(0, 0, 400, 400, fill='sienna')
Rect(100, 50, 200, 300, fill='ghostWhite')

# Draws all of the lines on the paper.
Line(200, 110, 200, 260, lineWidth=150, dashes=True)
Line(140, 325, 265, 325)
Line(125, 310, 135, 320, lineWidth=1)
Line(125, 320, 135, 310, lineWidth=1)

# Add the three labels to the contract.
### Place Your Code Here ###
Label('Contract', 200,80, size=18, font='orbitron', bold=True)
Label('Sign Here', 150,290, font='arial', italic=True)
Label('Sarah Smith', 190,315, size=20, font='cursive')