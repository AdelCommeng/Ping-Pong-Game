from turtle import Turtle,Screen
from paddle import Paddlef
from ball import Ball
import time
from score import Score
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)

player1=Paddlef(-350)
player2=Paddlef(350)
def moveup(xx):
    y = xx.ycor() + 20
    xx.goto(xx.xcor(), y)
def movedown(xx):
    y = xx.ycor() - 20
    xx.goto(xx.xcor(), y)
screen.listen()
screen.onkey(player1.moveup, "w")
screen.onkey(player1.movedown, "s")
screen.onkey(player2.moveup, "Up")
screen.onkey(player2.movedown, "Down")
ball =Ball()

game_on=True
scorep1=0
scorep2=0
s = Score()
while game_on:
    time.sleep(ball.move_speed) # Every bounce, the speed increases for fun!
    screen.update()
    ball.move()
    #Detect the bounce off the y axis
    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()
    #Detect collision with paddle
    if ball.distance(player2) < 50 and ball.xcor() > 320 or (ball.distance(player1) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        time.sleep(0.01)
    #Detect a score!
    if ball.xcor() > 380:
        ball.reset_game()
        s.leftscore()

    if ball.xcor() < -380:
        ball.reset_game()
        s.rightscore()



screen.exitonclick()
