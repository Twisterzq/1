x = 0
y = 0
def setup ():
    size (500,700)
def draw ():
    global x, y
    for step in 1,2,3,4,5,6,7,8,9:
        fill (random(0,255),random(0,255),random(0,255))
        ellipse (random(0,500),random(0,700),random(0,500),random(0,500))
    
