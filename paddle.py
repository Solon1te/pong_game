from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.pu()
        self.color("white")
        self.turtlesize(2.5, .5)
        self.goto(350, 0)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(350, new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(350, new_y)
