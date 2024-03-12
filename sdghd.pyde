x = 0
y = 20
color = 50
def setup ():
    size (500,500)
def draw ():
    global x, y
    fill (random(0,255),random(0,255),random(0,255))
    for y in 20,60,100,140,180,220,260,300,340,380,420,460:
        rect (x,y,20,20)
    x = x + 5
