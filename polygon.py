import turtle

def drawPolygon(t, sideLength, numSides):
    angle = 360 / numSides 
    for i in range(numSides):
        t.forward(sideLength)
        t.left(angle)

wn = turtle.Screen()
wn.bgcolor("yellow")
geo = turtle.Turtle()
geo.color("red")
drawPolygon(geo,30,10)  # draw a decagon

wn.exitonclick()
