x = 0
def setup ():
    size (500,500)
def draw ():
    global x
    for x in 50, 60, 70, 80, 90:
        fill (0,0,255)
        translate (x,x)
        ellipse (0,0,30,30)
