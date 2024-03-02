from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("white")
        self.goto(0,0)
        self.seth(37)
        self.move()

    def move(self):
        self.forward(10)
