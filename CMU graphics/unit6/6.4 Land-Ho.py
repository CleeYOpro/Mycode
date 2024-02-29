Rect(0, 0, 400, 200, fill='skyBlue')

island = Group(
    Oval(200, 200, 300, 80, fill='wheat'),
    Oval(200, 170, 200, 20, fill='green'),

    Polygon(235, 165, 245, 170, 250, 150, 250, 145, 260, 55, 240, 155,
            fill='sienna'),
    Star(255, 75, 50, 9, fill='limeGreen', roundness=50),
    Circle(230, 85, 6, fill='maroon'),
    Star(255, 75, 40, 8, fill='green', roundness=50),
    Circle(245, 80, 6, fill='maroon'),
    Circle(250, 100, 6, fill='maroon'),
    )
island.width = 20
island.height = 16
island.centerX = 200
island.bottom = 203

Rect(0, 200, 400, 200, fill='navy')

eyeglass = Group(
    Line(85, 280, 90, 410, fill='lightGrey', lineWidth=15),
    Line(50, 370, 60, 325, fill='silver', lineWidth=40),
    Line(70, 280, 60, 325, fill='silver', lineWidth=50),
    Line(70, 280, 80, 235, fill='silver', lineWidth=60),
    Line(90, 190, 80, 235, fill='silver', lineWidth=70)
    )

zoomedInGlass = Group(
    Circle(200, 200, 300, fill=None, border='dimGrey', borderWidth=100),
    Circle(200, 200, 200, fill='white', opacity=25)
    )
zoomedInGlass.visible = False
    
def onMousePress(mouseX, mouseY):
    # Increase the width and reposition the island's centerX.
    ### (HINT: The first test case will make the island big, so you can use
    #          the inspector.)
    ### Place Your Code Here ###
    island.width=300
    island.centerX=200
    # This resizes and repositions the height and bottom.
    island.height = 250
    island.bottom = 240

    # Update the the visibility of the eyeglass and zoomedInGlass shapes.
    ### Place Your Code Here ###
    zoomedInGlass.visible=True
    eyeglass.visible=False

def onMouseRelease(mouseX, mouseY):
    # Resizes and repositions the island.
    island.width = 20
    island.height = 16
    island.centerX = 200
    island.bottom = 203

    # Updates the the visibility of the eyeglass and zoomedInGlass shapes.
    zoomedInGlass.visible = False
    eyeglass.visible = True
