app.background = 'black'
stars = Group()
connections = Group()

def drawConstellation():
    # Creates the stars.
    for i in range(15):
        x = randrange(0, 400)
        y = randrange(0, 400)
        stars.add(
            Star(x, y, 3, 4, fill='white')
            )

    # Look at all pairs of stars that we can draw lines between.
    for star1 in stars:
        for star2 in stars:
            # When star1 and star2 are not the same star and star1 is more right
            # than star2, add connections between stars that are between 50 and
            # 150 pixels apart.
            ### (HINT: Use the distance function to determine how far apart
            #          the stars are!)
            if star1!=star2 and star1.centerX>star2.centerX:
                distance_between_stars=distance(star1.centerX, star1.centerY, star2.centerX, star2.centerY)
                if 50<distance_between_stars<150:
                    connections.add(Line(star1.centerX,star1.centerY,star2.centerX,star2.centerY,fill='grey', lineWidth=1))
        pass

    stars.toFront()

def onKeyPress(key):
    if (key == 'r'):
        stars.clear()
        connections.clear()
        drawConstellation()
