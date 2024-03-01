from turtle import Screen
from paddle import Paddle
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.listen()


paddle = Paddle()
screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")

screen.exitonclick()
