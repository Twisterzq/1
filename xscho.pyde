x = 50
y = 250
color = 50
def setup ():
    size (500,500)
def draw ():
    background (50)
    global x, y
    for x in 450, -100,-100,-100,-100:
        translate (100,x)
        ellipse (-50,0,50,50)
