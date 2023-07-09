from turtle import Screen
from Snake import Snake
import time
from Food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("nokia 3310")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    new_score = 0
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        new_score += 1
        food.refresh()
        snake.extend()
        score.Score_generator()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

    if (
            snake.head.xcor() > 290
            or snake.head.xcor() < -290
            or snake.head.ycor() > 300
            or snake.head.ycor() < -290

    ):
        game_is_on = False
        score.game_over()

screen.exitonclick()
