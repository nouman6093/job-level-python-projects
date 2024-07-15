import random
import turtle
from turtle import Turtle, Screen
import colorgram

#extracting colors from an image:
rgb_colors = []
colors = colorgram.extract('OIP.jpg', 21)   #write name of image file in your project folder
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    tu = (r,g,b)
    rgb_colors.append(tu)

t1 = Turtle()
t1.hideturtle()
t1.penup()
t1.speed("fastest")
turtle.colormode(255)
t1.setheading(220)
t1.forward(300)
t1.setheading(360)

for i in range(1, 101):
    t1.dot(20, random.choice(rgb_colors))
    t1.forward(50)

    if i % 10 == 0:
        t1.setheading(90)
        t1.forward(50)
        t1.setheading(180)
        t1.forward(500)
        t1.setheading(0)

screen = Screen()
screen.title("The Hirst Dot Painting")
screen.exitonclick()
