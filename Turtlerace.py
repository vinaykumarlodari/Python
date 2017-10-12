import turtle              # import the modules
from random import randint # to make the random movement of turtles use ranindt() from random module
wn = turtle.Screen()       # Create a screen
wn.bgcolor('yellow')

lance = turtle.Turtle()    # Create two turtles
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                  # Move the turtles to their starting point
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)

for i in range(80):
    andy.forward(randint(1,5))
    lance.forward(randint(1,5))
    
wn.exitonclick()
