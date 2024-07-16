from turtle import Turtle, Screen
import random
import time

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_parts = []

class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()

    def create_snake(self):
        for i in starting_positions:
            self.add_segment(i)

    def add_segment(self, i):
        t1 = Turtle("square")
        t1.color("white")
        t1.penup()
        t1.goto(i)
        self.snake_parts.append(t1)

    def extend(self):
        #this method adds a new segment to the snake
        self.add_segment(self.snake_parts[-1].position())

    def move(self):
        for i in range(len(self.snake_parts) - 1, 0, -1):
            self.snake_parts[i].goto(self.snake_parts[i - 1].pos())
            self.snake_parts[i].setheading(self.snake_parts[i - 1].heading())
        self.snake_parts[0].forward(20)

    def up(self):
        if self.snake_parts[0].heading() != 270:
            self.snake_parts[0].setheading(90)

    def down(self):
        if self.snake_parts[0].heading() != 90:
            self.snake_parts[0].setheading(270)

    def right(self):
        if self.snake_parts[0].heading() != 180:
            self.snake_parts[0].setheading(0)

    def left(self):
        if self.snake_parts[0].heading() != 0:
            self.snake_parts[0].setheading(180)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.speed("fastest")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

should_continue = True
while should_continue:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #collision with the food:
    if snake.snake_parts[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detecting collision:
    if snake.snake_parts[0].xcor() > 280 or snake.snake_parts[0].xcor() < -280 or snake.snake_parts[0].ycor() > 280 or snake.snake_parts[0].ycor() < -280:  #this means that snake has hit the wall
        should_continue = False
        scoreboard.game_over()

    #detecting collision with tail:
    for i in snake.snake_parts[1:]:
        if snake.snake_parts[0].distance(i) < 10:
            should_continue = False
            scoreboard.game_over()

screen.exitonclick()
