from turtle import Turtle, Screen
import time
from pong import Pong
from score import Scoreboard
from ball import Ball


screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)


score = Scoreboard()

pong = Pong((-380,0))
oppong = Pong((370,0))

ball = Ball()

screen.onkey(oppong.up, "Up")
screen.onkey(oppong.down, "Down")
screen.onkey(pong.up, "w")
screen.onkey(pong.down, "s")

dot_line = Turtle()
dot_line.color("white")
dot_line.right(90)
dot_line.penup()
dot_line.pensize(5)
dot_line.goto(0,300)
for x in range(15):
    dot_line.pendown()
    dot_line.forward(20)
    dot_line.penup()
    dot_line.forward(20)
dot_line.hideturtle()

loc = 0
c = 4

game = True

while game:
    c += 1
    screen.update()
    ball.move()
    pong.move()
    oppong.move()





    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(oppong) < 50 and ball.xcor() > 320 or ball.distance(pong) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_pscore()

    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_oscore()

    if score.o_score == 7 or score.p_score == 7:
        score.game_over()
        game = False
        screen.update()






screen.exitonclick()
