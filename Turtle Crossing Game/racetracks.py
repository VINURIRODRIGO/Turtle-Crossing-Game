from turtle import Turtle


class RacingTracks(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.x_cor = 500
        self.y_cor = -240
        self.create_tracks()

    def create_tracks(self):
        for _ in range(8):
            self.draw_tracks()
            self.y_cor += 70

    def draw_tracks(self):
        self.goto(self.x_cor, self.y_cor)
        self.setheading(180)
        for _ in range(25):
            self.penup()
            self.forward(20)
            self.pendown()
            self.forward(20)
            self.penup()
