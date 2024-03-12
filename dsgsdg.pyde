x = 0
y = 250
color = 50
def setup ():
    size (500,500)
def draw ():
    global x, y
    fill (random(0,255),random(0,255),random(0,255))
    for step in 1,2,3,4,5,6,7,8,9,10,11,12:
        translate (0,40)
        rect (x,-20,20,20)
    x = x + 5
