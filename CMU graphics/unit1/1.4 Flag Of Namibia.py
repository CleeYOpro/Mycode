# background
Rect(0, 0, 400, 400, fill='whiteSmoke')

# Draw the flag of Namibia.
### (HINT: The sun is drawn using one star and one circle with a border.)
### Place Your Code Here ###
Label("Namibia", 200,50, fill='black', size=30)
Rect(5,100,390,265, fill='white')
Polygon(5,325,5,365,65,365,395,140,395,100,335,100, fill=rgb(210,15,50))
Polygon(85,365,395,365,395,155, fill=rgb(0,150,65))
Polygon(5,100,5,310,315,100, fill=rgb(0,60,125))


Star(84,174,40,12, fill=rgb(255,215,0))
Circle(84,174,25, fill=rgb(255,215,0), border=rgb(0,60,125), borderWidth=5)
