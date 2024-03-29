app.background = 'darkBlue'

icon = Group(
    Label('DVD', 220, 200, fill='white', size=50, bold=True),
    Oval(220, 230, 110, 20, fill='white'),
    Label('video', 220, 230, fill='darkBlue', size=15)
    )
icon.dx = 5
icon.dy = 5

def onStep():
    # Move the icon by the amount indicated by icon.dx and icon.dy.
    icon.centerX+=icon.dx
    icon.centerY+=icon.dy
    
    # Reverse the direction of the icon if it reaches an edge of the canvas.
    ### Place Your Code Here ###
    if(icon.centerX>340):
        icon.dx=-5
    if(icon.centerY>370):
        icon.dy=-5
    if(icon.centerX<60):
        icon.dx=+5
    if(icon.centerY<30):
        icon.dy=+5
    pass
