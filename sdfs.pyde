x = 50
def setup():
    size(600, 600)
    
def draw():
    global x
    for x in 50, 110, 180 ,260,350:
        fill (0,255,0)
        ellipse (x,x,30,30)
