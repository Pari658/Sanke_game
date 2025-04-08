from turtle import Turtle,Screen
class Snake:
    def __init__(self):
        self.list=[]
        self.create()
    def create(self):
        i=0
        for x in range(3):
            tim=Turtle()
            self.list.append(tim)
            tim.shape("square")
            tim.color("white")
            tim.penup()
            tim.goto(i,0)
            i=i-20
    def add_seg(self,position):
        i=0
        tim=Turtle()
        self.list.append(tim)
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        i=i-20
    def extend(self):
        self.add_seg(self.list[-1].position())
    def move(self):
        for x in range(len(self.list)-1,0,-1):
            x_new=self.list[x-1].xcor()
            y_new=self.list[x-1].ycor()
            self.list[x].goto(x_new,y_new)
        self.list[0].forward(20)

    def left(self):
        self.list[0].setheading(180)
    def up(self):
        self.list[0].setheading(90)
    def right(self):
        self.list[0].setheading(0)
    def down(self):
        self.list[0].setheading(270)

