from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    pass


class Crosser(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_forward(self):
        self.forward(20)

    def go_to_start(self):
        self.goto(0, -180)

    def won(self):
        if self.ycor() > 190:
            return True


