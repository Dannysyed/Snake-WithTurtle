from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from highscore import Highscore
snake=Snake() #IMPORTING THE CUSTOM CLASS
food=Food() #importing
scoreboard=Scoreboard()
highscore=Highscore(scoreboard.score)
###### SCREEN SITTING ##########
screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.title('My Screen Game!')
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')
game_is_on=True
def gamereset():
    global game_is_on
    # print(game_is_on)
    snake.head.goto(0,0)
    screen.update()
    scoreboard.reset_score()
    print(snake.head.xcor())
    game_is_on=True


screen.onkey(gamereset,"q")

###### GAME LOGIC ##########

while game_is_on:
    screen.update()
    time.sleep(0.1) 
    snake.move()
    print('hi')
  
    ####collision
    if snake.head.distance(food)<15:
        print('asdfa')
        food.change_location()
        scoreboard.increase_score()
        screen.update()
        snake.extend()
        highscore=Highscore(scoreboard.score)
    if snake.head.xcor()> 288 or snake.head.xcor() < -288 or snake.head. ycor()> 288 or snake.head.ycor() < -288:
        scoreboard.game_over()
        game_is_on=False
    
   
 
print(snake.head.xcor())
screen.exitonclick()
