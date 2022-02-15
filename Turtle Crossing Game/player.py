from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("red")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_forward(self):
        if self.ycor() != FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

    def goto_start(self):
        self.goto(0, -280)