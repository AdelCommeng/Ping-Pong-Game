from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_player_score=0
        self.right_player_score=0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.left_player_score, align="center", font=('Arial', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.right_player_score, align="center", font=('Arial', 80, 'normal'))
    def leftscore(self):
        self.clear()
        self.left_player_score+=1
        self.update_score()
    def rightscore(self):
        self.clear()
        self.right_player_score += 1
        self.update_score()




