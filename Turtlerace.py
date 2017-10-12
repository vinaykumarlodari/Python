import turtle              # import the modules
from random import randint # to make the random movement of turtles use ranindt() from random module
wn = turtle.Screen()       # Create a screen
wn.bgcolor('cyan')


t = turtle.Turtle()
t.penup()
t.goto(-70,100)
t.pendown()

for i in range(11):
    t.hideturtle()
    t.speed(100)
    t.write(i)
    t.right(90)
    t.forward(200)
    t.write(i)
    t.right(180)
    t.forward(200)
    t.right(90)
    t.penup()
    t.forward(20)
    t.pendown()
    

lance = turtle.Turtle()         # Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                       # Move the turtles to their starting point
lance.up()
andy.goto(-100,30)
lance.goto(-100,0)

for i in range(80):
    andy.forward(randint(1,5))
    lance.forward(randint(1,5))
    
wn.exitonclick()
