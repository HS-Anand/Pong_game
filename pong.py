from turtle import Turtle


class Pong(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.left(90)
        self.goto(position)

    def up(self):
        self.setheading(90)

    def down(self):
        self.setheading(270)

    def move(self):
        if self.ycor() == 250 and self.heading() == 90:
            self.stop()
        elif self.ycor() == -240 and self.heading() == 270:
            self.stop()
        else:
            self.forward(5)

    def stop(self):
        self.forward(1)
        self.backward(1)





