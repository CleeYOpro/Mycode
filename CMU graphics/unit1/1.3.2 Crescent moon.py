# Draws the background.
Rect(0, 0, 400, 400, fill=rgb(30, 30, 30))

# Draw the moon and clouds.
### (HINT: Use two circles for the moon!)
### Place Your Code Here ###
Circle(200,175,100, fill=gradient('lightGrey','grey','grey', start='left'))
Circle(235,140,100, fill=rgb(30,30,30))
Oval(200,305,250,100, fill=rgb(90,90,90), opacity=80)
Oval(280,280,125,80, fill=rgb(90,90,90), opacity=80)
Oval(215,350,100,40, fill=rgb(90,90,90), opacity=80)
Oval(115,270,175,120, fill=rgb(90,90,90), opacity=80)