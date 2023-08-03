from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Syd's Snake Game!")
screen.tracer(0)

# creates a snake object instance.
new_snake = Snake()

# creates a food object instance.
food = Food()

# creates a scoreboard object instance.
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=new_snake.move_up, key="w")
screen.onkey(fun=new_snake.move_down, key="s")
screen.onkey(fun=new_snake.move_left, key="a")
screen.onkey(fun=new_snake.move_right, key="d")

game_is_on = True
while game_is_on:
    # refresh the screen.
    screen.update()
    # delay the refresh.
    time.sleep(0.1)
    new_snake.move()

    # detect collision with food.
    if new_snake.head.distance(food) < 15:
        # generate a new food item.
        food.refresh()
        # add to the snake's length.
        new_snake.extend()
        # add to score and update the scoreboard.
        scoreboard.add_score()

    # detect collision with wall.
    if new_snake.head.xcor() > 285 or new_snake.head.xcor() < -285 or new_snake.head.ycor() > 285 or new_snake.head.ycor() < -285:
        scoreboard.reset_highscore()
        new_snake.reset_snake()
        # game_is_on = False
        # scoreboard.game_over()

    # detect collision with tail. slice the list to bypass collision with itself.
    for snake_index in new_snake.snake_bodies[1:]:
        # check if the head has collision with any of the snake body.
        if new_snake.head.distance(snake_index) < 10:
            scoreboard.reset_highscore()
            new_snake.reset_snake()
            # game_is_on = False
            # scoreboard.game_over()


screen.exitonclick()
