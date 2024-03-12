x = 30
y = 250
color = 50
def setup ():
    size (500,500)
def draw ():
    background (50)
    global x, y
    x = x + 1
    for step in 1,2,3,4,5:
        translate (100,100)
        rect (-50,-50,x,x)
