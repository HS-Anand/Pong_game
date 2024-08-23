from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 48, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p_score = 0
        self.o_score = 0
        self.update_scoreboard()

    def go(self):
        self.goto(40, 240)

    def update_scoreboard(self):
        self.goto(-40, 240)
        self.write(f"{self.p_score}", align=ALIGNMENT, font=FONT)
        self.goto(40, 240)
        self.write(f"{self.o_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_pscore(self):
        self.p_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_oscore(self):
        self.o_score += 1
        self.clear()
        self.update_scoreboard()
