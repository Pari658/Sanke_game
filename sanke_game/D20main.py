from turtle import Screen
from D20Snake import Snake
from D20Food import Food
from D20score import scoreboard
import time


screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
sco=scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
a=0
while True:
    snake.move()
    screen.update()
    if snake.list[0].distance(food)<15:
        food.refresh()
        snake.extend()
        sco.inc()
    if snake.list[0].xcor()>280 or snake.list[0].xcor()< -280 or snake.list[0].ycor()>280 or snake.list[0].ycor()<-280:
        sco.game_over()
        break
    for x in snake.list:
        if x==snake.list[0]:
            pass
        elif snake.list[0].distance(x)<10:
            sco.game_over()
            a=1
            break
    if a==1:
        break
    time.sleep(0.1)

screen.exitonclick()