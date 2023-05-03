from turtle import Turtle, Screen, colormode
import random

colormode(255)


screen = Screen()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

screen.setup(600, 600)

turtles = []
y = -200
for i in range(10):
    new_turtle = Turtle(shape = "square")
    new_turtle.penup()
    new_turtle.color(random_color())
    new_turtle.speed("fastest")
    turtles.append(new_turtle)
    new_turtle.goto(-280, y)  
    y+=40

# turtles.stamp()

print(turtles)

finish = False

while True:
    for turtle in turtles:
        turtle.forward(random.randint(1, 20))
        if turtle.xcor() > 250:
            turtle.write("I won", font=("Arial", 33, "bold"))
            finish = True
            break
    if finish:
        break

screen.exitonclick()

Screen().done()