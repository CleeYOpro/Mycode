# Draws the background.
Rect(0, 0, 400, 400, fill='paleGreen')

# Draw the mushroom cap.
### Place Your Code Here ###
Oval(200,190,300,280, fill=rgb(250,40,40))
Rect(0,210,400,120, fill='paleGreen')
Oval(200,210,300,140, fill=gradient(rgb(250,40,40), rgb(150,30,30,), start='top'))
Circle(200,135,55, fill='snow')
Oval(90,190,65,80, fill=gradient('white', 'gainsboro', start='right'), opacity=95)
Oval(310,190,65,80, fill=gradient('white', 'gainsboro', start='left'), opacity=95)

# Draw the Mushroom's face.
### Place Your Code Here ###
Oval(200,270,180,120, fill=gradient('cornSilk', 'wheat'))
Oval(200,280,180,90, fill=gradient('cornSilk', 'wheat'))
# Draw the Mushroom's eyes.
### Place Your Code Here ###
Circle(175,250,8, fill='dimGrey')
Rect(167,250,16,25, fill=gradient('dimGrey', 'black', start='top'))
Circle(175,275,8, fill='black')
Oval(175,252,8,15, fill='white')
Circle(225,250,8, fill='dimGrey')
Rect(217,250,16,25, fill=gradient('dimGrey', 'black', start='top'))
Circle(225,275,8, fill='black')
Oval(225,252,8,15, fill='white')