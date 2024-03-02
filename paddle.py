from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        self.x = x
        super().__init__()
        self.pu()
        self.shape("square")
        self.color("white")
        self.turtlesize(5, 1)
        self.goto(self.x, 0)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.x, new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.x, new_y)
