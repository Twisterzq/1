x = 0
y = 0
def setup ():
    size (550,550)
def draw ():
    global x
    for x in 50, 150, 250, 350, 450:
        rect (x,250,50,50)
    for y in 50, 150, 250, 350, 450:
        rect (250,y,50,50)
