#slide counter
app.current_slide=1
######################################################################################1st slide
sc0 = Group(
    #green background
    Rect(0,100,400,200, fill = rgb(72,119,60)),
    #sdg logo
    Rect(100,100,200,200, fill = rgb(72,119,60), border='white', borderWidth=7),
    Circle(200,200,50, fill = 'white'),
    Polygon(149,199,169,201,181,206,178,223,169,224,169,238,138,247, fill = rgb(72,119,60)),
    Polygon(181,206,191,202,197,208,205,207,205,199,216,196,227,197,236,204,234,217,238,228,257,246,237,172,215,166,201,163,197,172,
    185,178,177,186, fill = rgb(72,119,60)),
    #starting titles and intro
    Label('The World', 200,200, size = 15, bold = True),
    Label('SDG 13: TAKE CLIMATE ACTION', 200,325, size=15, font = 'montserrat', bold= True),
    Label('What? Climate Change?', 200,345, size=25, font = 'montserrat', bold= True),
    Label('press (1) to move on to next slide', 200,365, size=10, font = 'montserrat')
    )
    
############################################################################################################2nd slide

#this is the sun ray effect function for slide 2        
def ray_effect():
    #check if it is the 2nd Slide
    if app.current_slide == 2:
        #check if the background opacity(used for timing) if its less than = to 0.2(the time)
        if timebackgr.opacity <= 0.2:
            # add rays to the respective groups with decreasing opacity
            r1.add(Line(25,25,25,75, fill = 'darkOrange', lineWidth = 20, opacity = 50))
            r2.add(Line(25,25,75,25, fill = 'darkOrange', lineWidth = 20,opacity = 50))
            r3.add(Line(25,25,25,-25, fill = 'darkOrange', lineWidth = 20, opacity = 50))
            r4.add(Line(25,25,-25,25, fill = 'darkOrange', lineWidth = 20, opacity = 50))
            #increase opacity (what im using as time here) gradually
            timebackgr.opacity += 0.001
        else:
            #make the info text visible if time has run out
            direc.visible = True
        
        #move each ray group in different directions         
        for i in [r1]:
            i.centerY+=6
            i.centerX+=2
            # clear the group when it reaches a certain position
            if i.centerY >= 350:
                i.clear()
                
        for i in [r2]:
            i.centerY+=5
            i.centerX+=5
            if i.centerY >= 350:
                i.clear()
                
        for i in [r3]:  
            i.centerY+=4
            i.centerX+=5
            if i.centerY >= 350:
                i.clear()
                
        for i in [r4]:
            i.centerY+=6
            i.centerX+=4
            if i.centerY >= 350:
                i.clear()

#groups to hold the ray functions
r1=Group()
r2=Group()
r3=Group()
r4=Group()

#the info text
direc = Group(
        Label('Sunlight enters Earth\'s atmosphere as solar radiation.',200,200,size = 14,fill= 'white'),
        Label('What reaches the suface of the Earth is radiated back as heat.',200,215,size = 14, fill= 'white'),
        Label('Press (2) to go to the next slide',200,230,size = 14, fill= 'white')
        )
direc.visible = False
#back ground used as timethat increases opacity very slightly
timebackgr = Rect(0,0,400,400, fill='gainsboro', opacity=0)

#################################################################################3rd slide
#Group to hold sun rays and heat elements
rays2 = Group()
heat = Group()

#Rectangle that represents smog that fills up as greenhouse gases are emmited
#also used as timer for how long rays and heat stay on slide
smogger = Rect(0,0,400,400, fill='darkGray', opacity=0)

#function to add rays to the rays2 group
def addrays(x1,y1,x2,y2,colour,linewidth):
    # a loop to add 8 rays to the rays2 group 
    for i in range(8):
        rays2.add(Line(x1,y1,x2,y2,fill=colour,lineWidth=linewidth))
        x1+=50
        x2+=50

#label to show info on what sunrays are
sunray = Label('Yellow --> Sun rays', 246,340,fill='yellow',size = 25, bold = True, visible = False)

#label to show info on what heat is
showheat = Label('Red --> This is the heat trying to leave Earth', 200,275, fill='Red',size = 17, bold = True,visible = False)

#displays information at the end of the 3rd slide
endOf3rdSlide = Group(
    Label('Smog.',200,135,size = 30, bold = True),
    Label('The air polution from human emmited greenhouse gases ',200,200,size = 15),
    Label('gets so bad that heat cannot leave Earth\'s atmosphere.',200,215,size = 15),
    Label('Press (3) to move on',200,230,size = 15)
    )
endOf3rdSlide.visible= False
#initialy set this to false so that it appears at right time
################################################################################
#Group to add shapes to for 4th slide
liq = Group()

################################################################################

# creating 3 polygons to reprsent icecaps with inital settings
ice1 = Polygon(0,20,200,100,340,220,0,220, fill= gradient(rgb(206,216,225), rgb(168,191,215), rgb(132,177,194), start = 'top'), opacity= 100, visible = False)
ice2 = Polygon(160,260,240,180,360,220,340,260, fill= gradient(rgb(206,216,225), rgb(168,191,215), rgb(132,177,194), start = 'top'),opacity= 100, visible = False)
ice3 = Polygon(0,220,140,200,280,340,0,340, fill= gradient(rgb(206,216,225), rgb(168,191,215), rgb(132,177,194), start = 'top'),opacity= 100, visible = False)
#instructions for user to hold down right to watch the Antartic ice shelf melt
direct = Label('Hold down the right arrow to watch the Antartic ice shelf melting',200,380,size = 13, visible = False)

#function to sim the melting ice
def meltIce():
    # individual settings for every iceberg
    if ice1.height > 0:
        if ice1.height<100 and ice1.width>0:#checks heigh and width to decrease them
            ice1.width-=10
        else:
            ice1.height -= 10
        
        if ice1.width == 0:
            #as ice1's width last to hit 0 (melt) The instruction label gone
            
            direct.visible = False
            #consequences of climate change and melting poles
            Label('Melting Poles.',200,135,size = 30, bold = True)
            Label('Cause global sea levels to rise, flooding coastal areas.',200,200,size = 14)
            Label('Cause more severe and frequent extreme weather events.',200,215,size = 14)
            Label('Cause distrupted ocean currents and temperatures.',200,230,size = 14)
            Label('Causes damage to infrastructure and agriculture.',200,245,size = 14)
            Label('Could directly cost $1.7 - 3.1 trillion per year up to 2050.',200,260,size = 14)
            Label('STOP CLIMATE CHANGE',200,285,size = 17)
            #the simulation of sdg 13 is ove and stop the app
            app.stop()
    if ice2.height > 0:
        if ice2.height < 5:
            ice2.height=0
        else:
            ice2.height -= 5
    if ice3.height > 0:
        ice3.height -= 10
#hold function to handle the right arrow
def onKeyHold(keys):
    if app.current_slide == 5:
        if 'right' in keys:
            meltIce()
################################################################################



#on each key press move to the next slide        
def onKeyPress(keys):
    #if 1 is pressed
    if '1' in keys:
        #start slide 2
        app.current_slide=2
        #black bacground for space
        Rect(0,0,400,400, fill = 'black')
        Rect(0,0,400,400, fill ='black')
        #the sun
        Circle(25,25,70,fill ='orange')
        Label('Sun', 20,10, size = 19, bold = True)
        #image of Earth
        image= Image('cmu://744032/28858070/Screenshot+2024-02-15+105703.png', 200,230)
        image.width /= 2
        image.height /= 3
        image.right = 400
        image.bottom = 400
    
    #if 2 is pressed
    if '2' in keys:
        #start slide 3
        app.current_slide=3
        # Display image of factories and greenhouse gas emmitors
        image= Image('cmu://744032/28863759/Screenshot+2024-02-15+122202.png', 0,150)
        image.width /= 2
        image.height /= 4
        image.bottom = 400
        # Draw shapes that represent the atmosphere and sun rays
        Rect(0,0,400,250, fill = rgb(239,215,186))
        Oval(57,41,180,120, fill='darkGray')
        Circle(155,14,50,fill='darkGray')
        Circle(221,36,50,fill='darkGray')
        Circle(280,35,50,fill='darkGray')
        Oval(340,12,150,140,fill='darkGray')
    #if 3 is pressed
    if '3' in keys:
        #start slide 4
        Rect(0,0,400,400, fill = 'black')
        app.current_slide=4
        # draw shapes representing a thermometer and trapped heat
        Rect(170,50,60,220, fill='silver', border='dimGray', borderWidth = 8)
        Circle(200,320, 60, fill ='silver', border = 'dimGray', borderWidth = 8)
        Circle(200,320, 52, fill ='red')
        Rect(175,270,50,50,fill='red')
        Label('The trapped heat makes the entire planet warmer. The rate at which',200,300,size = 13,fill= 'white')
        Label('this is happening is pretty frightening. The Earth is about 1° C',200,313,size = 13, fill= 'white')
        Label('hotter than it was in pre-industrial times. We don\'t want to exceed 2°',200,326,size = 13, fill='white')
        Label('as that could have really bad consequences and most scientists say',200,339,size = 13, fill='white')
        Label('that we could get to 1.5° by 2030. Press (4) to move on',200,352,size = 13, fill='white')
    #if 4 is pressed
    if '4' in keys:
        #clear previous slides shapes start this slide 5
        liq.clear()
        app.current_slide = 5
        #blu backround and gradient water
        Rect(0, 0, 400, 300, fill='lightSkyBlue')
        Rect(0, 150, 400, 300, fill=gradient('steelBlue', 'darkCyan', start='right-bottom'))
        #display each ice shelf polygons and the intstructions
        ice1.visible = True
        ice2.visible = True
        ice3.visible = True
        direct.visible = True
        #bring the ice and instruction to the front of the background
        ice1.toFront()
        ice2.toFront()
        ice3.toFront()
        direct.toFront()
        
################################################################################        
#step function
def onStep():
    if app.current_slide == 2:#check if current slide is 2
        # bring ray shapes and direction labels to the front
        r1.toFront()
        r2.toFront()
        r3.toFront()
        r4.toFront()
        direc.toFront()
        # call the function that creates the rays for slide 2
        ray_effect()
    if app.current_slide == 3:#check if current slide is 3
        #bring rays heat and smog to the front
        rays2.toFront()
        heat.toFront()
        smogger.toFront()
        #add sun rays
        addrays(8,18,16,16,'yellow',2)
        
        # draw heat
        heat.add(Line(5,275,75,275, fill = 'red', lineWidth = 2))
        heat.add(Line(100,275,175,275, fill = 'red', lineWidth = 2))
        heat.add(Line(200,275,275,275, fill = 'red', lineWidth = 2))
        heat.add(Line(300,275,395,275, fill = 'red', lineWidth = 2))
        #labels for what sunrays and heat is
        sunray.visible = True
        showheat.visible = True
        
        #increase the intensity of smog until opacity is 90
        if smogger.opacity<90:
            smogger.opacity += 0.5
        
        # Move rays downward until y is 340
        if rays2.centerY <= 340:
            rays2.centerY += 5
            rays2.centerX+= 1
        else:
            rays2.clear()
        
        # move heat lines upward until y is 95
        if heat.centerY >= 95:
            heat.centerY -= 10
        else:
            heat.clear()
        
        # if smog opacity reaches 90, clear rays and heat, display the end of the 3rd slide
        if smogger.opacity == 90:
            rays2.clear()
            heat.clear()
            sunray.visible = False
            showheat.visible = False
            endOf3rdSlide.visible= True
    
    if app.current_slide == 4:#check if current slide is 4
        liq.toFront()
        #red rectangle representing red liquid inside the thermometer
        liq.add(Rect(175,270,50,10,fill='red'))
        liq.centerY-=3
        # if the top of liquid is less than = to 58 clear and repeat
        if liq.top<=58:
            liq.clear()