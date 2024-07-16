import random
from turtle import Turtle, Screen

s1 = Screen()
s1.setup(500,400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

while True:
    bet = s1.textinput("Make a bet!", "Which turtle will win the race?")
    if bet in colors:
        break
    else:
        print("please enter from following: red, orange, yellow, green, blue, purple")

y_positions = [-70, -40, -10, 20, 50, 80]
speed = [1.0, 1.1, 1.2, 1.3, 1.4]
all_turtles = []

for i in range(1,6):
    t1 = Turtle("turtle")
    t1.penup()
    t1.goto(-230,y_positions[i])
    t1.color(colors[i])
    t1.speed(random.choice(speed))
    t1.speed(random.choice(speed))
    all_turtles.append(t1)

should_continue = True
while should_continue:
    for i in all_turtles:
        i.forward(random.randint(1,11))
        if i.xcor() > 200:
            should_continue = False
            if bet == i.pencolor():
                print(f"The {i.pencolor()} turtle is the winner!")
            else:
                print(f"Sorry, The {i.pencolor()} turtle is the winner!")

s1.exitonclick()
