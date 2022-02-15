from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 1
        self.hideturtle()
        self.displaying_level()

    def displaying_level(self):
        self.pencolor("white")
        self.penup()
        self.goto(-280, 270)
        self.pendown()
        self.write(f"level - {self.count}", True, align="left", font=FONT)

    def new_level(self):
        self.clear()
        self.count += 1
        self.displaying_level()

    def game_over(self):
        self.penup()
        self.clear()
        self.goto(0, 270)
        self.write("GAME OVER", True, align="center", font=FONT)
