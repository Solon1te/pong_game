from turtle import Screen
from paddle import Paddle
from ball import Ball
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
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    ball.move()
    time.sleep(.04)
    screen.update()


screen.exitonclick()
