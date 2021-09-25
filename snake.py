import turtle as t
SNAKE_START = [(0, 0), (-20, 0), (-40, 0)]
MOVE_PACE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_bodies = []
        self.create_snake()             # when the Snake class is called, this'll also call create_snake function to run
        self.head = self.snake_bodies[0]
        self.head.color("light pink")

    def create_snake(self):
        for i in SNAKE_START:
            self.add_body(i)

    def add_body(self, i):
        snake_body = t.Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(i)
        self.snake_bodies.append(snake_body)

    def extend_body(self):
        # add a new body to the snake.
        self.add_body(self.snake_bodies[-1].position())

    def reduce_body(self):
        # reduce a body from the snake
        self.snake_bodies[-1].hideturtle()
        self.snake_bodies.pop()

    def move(self):
        for i in range(len(self.snake_bodies) - 1, 0, -1):
            x = self.snake_bodies[i - 1].xcor()
            y = self.snake_bodies[i - 1].ycor()
            self.snake_bodies[i].goto(x, y)

        self.head.forward(MOVE_PACE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

