from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("circle")
        self.color("white")
        self.goto(0,0)
        self.seth(45)
        self.move()
        self.move_speed = 0.1

    def move(self):
        self.forward(10)

    def bounce_y(self):
        new_angle = 360 - self.heading()
        self.seth(new_angle)

    def bounce_x(self):
        new_angle = 180 - self.heading()
        self.seth(new_angle)
        self.move_speed *= 0.8

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = .1
        self.bounce_x()
