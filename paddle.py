from turtle import Turtle
class Paddlef(Turtle):
    def __init__(self,x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x, 0)
    def moveup(self):
        y=self.ycor()+20
        self.goto(self.xcor(),y)
    def movedown(self):
        y=self.ycor()-20
        self.goto(self.xcor(),y)


