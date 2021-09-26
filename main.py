import turtle as t
import snake as s
import food as f
import scoreboard as sb
import random
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)                                     # movement animation-off of single snake bodies

snake = s.Snake()
scoreboard = sb.Scoreboard()
food = f.Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

x = 0
y = 0
game_is_on = True
while game_is_on:
    screen.update()                                  # as animation is off, we need to update the movement manually
    time.sleep(0.1)                                  # slowing down the update of movement
    snake.move()

    # Detecting the collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_body()
        scoreboard.increase_sb()

    # everything about poison
    if scoreboard.score >= 5:
        if x == 0:
            poison = f.Poison()
            x += 1
        poison.move()

        if poison.xcor() > 300:
            random_y = random.randint(-280, 280)
            poison.goto(-(poison.xcor()), random_y)

        # Detecting the collision with poison
        if snake.head.distance(poison) < 15:
            if y < 1:
                poison.refresh()
            else:
                poison.goto(2000, 2000)

            for i in range(5):
                if len(snake.snake_bodies) > 3:
                    snake.reduce_body()
                if scoreboard.score > 5:
                    scoreboard.decrease_sb()
            y += 1

    # Detecting the collision with wall and returning from other side
    if snake.head.xcor() < -320:
        snake.head.goto(300, snake.head.ycor())

    if snake.head.xcor() > 300:
        snake.head.goto(-(snake.head.xcor()), snake.head.ycor())

    if snake.head.ycor() < -320:
        snake.head.goto(snake.head.xcor(), 300)

    if snake.head.ycor() > 300:
        snake.head.goto(snake.head.xcor(), -(snake.head.ycor()))

    # Detecting collision with own tail
    for i in snake.snake_bodies[1:]:
        if snake.head.distance(i) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()