import turtle              # import the modules

wn = turtle.Screen()       # Create a screen
wn.bgcolor('yellow')

def drawSquare(t, sz):
    """Make turtle t draw a square of sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)

ttle = turtle.Turtle()        
ttle.color("blue")
ttle.shape("turtle")
drawSquare(ttle,100)
wn.exitonclick()
