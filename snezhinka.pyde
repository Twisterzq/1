x = 250
y = 250
color = 50
def setup ():
    size (500,500)
def draw ():
    background (50)
    global x, y,color 
    color = color + 1
    fill (color)
    ellipse (x,250,50,50)
    ellipse (x-100,250,50,50)
    ellipse (x-200,250,50,50)
    ellipse (x+100,250,50,50)
    ellipse (x+200,250,50,50)
    ellipse (x,150,50,50)
    ellipse (x,50,50,50)
    ellipse (x,350,50,50)
    ellipse (x,450,50,50)
    ellipse (x-100,150,50,50)
    ellipse (x+100,350,50,50)
    ellipse (x-100,350,50,50)
    ellipse (x+100,150,50,50)
    ellipse (x-200,50,50,50)
    ellipse (x+200,50,50,50)
    ellipse (x-200,450,50,50)
    ellipse (x+200,450,50,50)
    x = x - 3
    if x <= -250:
        x = 750
    if color >= 255:
        color = 50
