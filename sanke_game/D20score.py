from turtle import Turtle
class scoreboard(Turtle): 
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.write(f"Score is:{self.score}",align="center",font=("Arial",20,"normal"))

    def inc(self):
        self.score+=1
        self.clear()
        self.write(f"Score is:{self.score}",align="center",font=("Arial",20,"normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write("GAME OVER",align="center",font=("Arial",20,"normal"))