#Click to see the lava color darken.

app.background = gradient('skyBlue', rgb(235, 235, 235), start='top')

app.volcanoHasErupted = False

# volcano
lava = Oval(200, 120, 90, 20, fill=rgb(255, 200, 0), border='peru',
            borderWidth=4)
lava.green = 200

rock = Polygon(0, 400, 0, 380, 50, 340, 70, 300, 125, 225, 140, 180, 153, 120,
               175, 125, 200, 120, 220, 108, 235, 105, 247, 110, 255, 175, 270,
               210, 310, 250, 350, 325, 400, 375, 400, 400,
               fill=gradient('peru', 'sienna', start='top'))

# lava explosion
burst = Polygon(100, 0, 310, 0, 260, 30, 245, 60, 240, 110, 235, 105, 220,
                108, 200, 120, 175, 125, 160, 120, 150, 60, 130, 25,
                fill=gradient(rgb(255, 200, 75), rgb(235, 10, 20), start='bottom'),
                visible=False)

def drawSpill():
    Polygon(153, 120, 175, 125, 165, 195, 145, 260,
            80, 315, 125, 260, 150, 200, 155, 160,
            fill=gradient(rgb(255, 200, 75), rgb(235, 10, 20), start='top'))
    Polygon(200, 120, 220, 108, 230, 160, 230, 210,
            240, 240, 310, 345, 245, 280, 215, 225, 210, 160,
            fill=gradient(rgb(255, 200, 75), rgb(235, 10, 20), start='top'))
    Polygon(235, 105, 247, 110, 255, 175, 270, 210,
            310, 250, 255, 215, 240, 170, 240, 130,
            fill=gradient(rgb(255, 200, 75), rgb(235, 10, 20), start='top'))

def onMousePress(mouseX, mouseY):
    # Use rgb values and a provided custom property to change the fill of lava
    # at the top of the volcano so that it appears more red. Don't let any
    # value in the rgb become negative.
    ### (HINT: Decrease the value of green to make red more apparent!)
    ### (HINT: We defined a custom property that may be helpful.)
    if(app.volcanoHasErupted==False):
        if(lava.green>0):
            lava.green-=40
            lava.fill=rgb(255, lava.green, 0)
        else:
            app.volcanoHasErupted=True
            drawSpill()
            burst.visible=True
            app.background=gradient('lightSlateGrey','lightGrey', start='top')
    # If there was no more green in the lava when the mouse was clicked,
    # the volcano should erupt if it hasn't already. The volcano should
    # only erupt once.
    ### (HINT: Use a provided app custom property to check if it has erupted.)
    
    pass
