# Fill me in!
app.background = gradient('seaGreen','saddleBrown','saddleBrown', start='center')


#welcome and sdg info code
welcome = Group(
    Rect(50, 100, 300, 200, fill=gradient('deepSkyBlue','deepSkyBlue','dodgerBlue', start="center")),
    Label("SDG 6: Ensure availability and sustainable ", 200,190, size=12, font='arial'),
    Label('management of water and sanitation for all.', 200,210, size=12, font='arial'),
    Label('Press "q" to continue', 200,230, size=12, font='arial'))

#more information about clean water
welcomeinfo = Group(
    Rect(42, 100, 315, 200, fill=gradient('deepSkyBlue','deepSkyBlue','dodgerBlue', start="center")),
    Label("About 80% of all global wastewater is discharged into", 200,180, size=12, font='arial'),
    Label('water bodies without proper treatment. There is much need', 200,195, size=12, font='arial'),
    Label('for initiatives focused on sustainable water management.', 200,210, size=12, font='arial'),
    Label('Press "w" to continue', 200,230, size=10, font='arial'))
welcomeinfo.visible=False

#game instructions
Game = Group(
    Rect(50, 100, 300, 200, fill=gradient('deepSkyBlue','deepSkyBlue','dodgerBlue', start="center")),
    Label('Click on the land (Brown) to add River filteration facilities', 200,190, size=12, font='arial'),
    Label('Once you add enough, the river will gradually get cleaner', 200,210, size=12, font='arial'),
    Label('Press "e" to continue', 200,230, size=12, font='arial'))
Game.visible=False


#river
river = Rect(0, 100, 400, 200, fill='olive', opacity= 100,visible=False)


#Alert Label: prvides warning message to the user not to drown the water purification facility
ALERT = Label("MAKE SURE NOT TO DROWN OUR WATER PURIFICATION FACILITY", 200,200, 
    size=11, font='monospace',bold=True, visible = True)
ALERT.visible= False


#Mouse event #1
def onKeyPress(key):
    if (key == 'q'):
        welcome.visible = False
        welcomeinfo.visible=True
    if (key == 'w'):
        welcomeinfo.visible = False
        Game.visible = True
    if (key == 'e'):
        Game.visible = False
        river.visible=True


# initialize count
app.count=0

# Mouse event #2
def onMousePress(x, y):
    #check if the click  is within specified range
    if (y>=330) or (y<=70):
        ALERT.visible=False
        #create water purification center elements
        drawWPC(x,y)#call one
        #Increment count based on the number of clicks
        app.count+=1
    elif (y>399): #extra random conditional to get the 2 calls to function
        drawWPC(x,y)#call 2
    else:
        ALERT.visible =True
        
# This is my self defined function 1
def drawWPC(x,y):#my function takes 2 parameters
    #create Water purification center elements
    Rect(x-50,y-15, 180, 60, fill='gainsboro', border='dimGray'),
    Rect(x,y, 80, 30, fill='gainsboro', border='dimGray'),
    Label("WATER PURIFICATION CENTER", x+40,y+15, size=11, font='monospace',bold=True)
    if app.count ==0:#river changes (gets cleaner) as more centers are added
        river.opacity = 50
        Rect(0, 100, 400, 200, fill='darkCyan', opacity= 50)
    elif app.count ==1:
        river.opacity = 50
        Rect(0, 100, 400, 200, fill='darkCyan', opacity= 100)
    elif app.count == 2:
        Rect(0, 100, 400, 200, fill='dodgerBlue', opacity= 75)
        Rect(0, 100, 400, 200, fill='darkSeaGreen', opacity= 25)
    else:
        #final state of the river fully clean
        Rect(0, 100, 400, 200, fill='blue', opacity= 75)
        clean = Label("THE RIVER IS CLEAN!", 200,190, size=20,fill='white', font='monospace',bold=True)
        app.stop() #stop the  sim
        