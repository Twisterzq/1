razmer = 0
def setup():
    size(600, 900)
    
def draw():
    for razmer in 5, 15, 20 ,50, 80:
        fill (255,0,0)
        translate(0, 150)
        rect (300,0,razmer,razmer)
