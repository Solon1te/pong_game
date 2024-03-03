from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

ball = Ball()
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
scoreboard = Scoreboard()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    current_speed = .04
    ball.move()
    time.sleep(ball.move_speed)
    screen.update()

    # check for collisions with top and bottom walls
    if ball.ycor() > 280:
        ball.bounce_y()
    if ball.ycor() < -280:
        ball.bounce_y()

    # check for collisions with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        time.sleep(current_speed)

    # check for paddle misses
    if ball.xcor() > 420:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -420:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
