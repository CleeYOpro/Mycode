# Draws the background and blank cards.
Rect(0, 0, 400, 400, fill=gradient('darkGreen', 'forestGreen', start='top'))
Rect(90, 50, 180, 280, fill=rgb(245, 245, 245))
Rect(130, 70, 180, 280, fill='white')

# Draw the suit and numbers on top of the cards.
### Place Your Code Here ###
Label('2', 110,70, fill='crimson', font='monospace', size=30, bold=True)
Label('A', 280,290, fill='crimson', font='monospace', size=30, bold=True)
Label('A', 150,90, fill='crimson', font='monospace', size=30, bold=True)
Star(110,100,15,4, fill='crimson', roundness=65)
Star(150,120,15,4, fill='crimson', roundness=65)
Star(220,210,25,4, fill='crimson', roundness=65)
Star(280,320,15,4, fill='crimson', roundness=65)