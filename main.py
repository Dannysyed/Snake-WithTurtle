from turtle import Turtle,Screen
import time
from snake import Snake
snake=Snake() #IMPORTING THE CUSTOM CLASS

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


###### GAME LOGIC ##########
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1) 
    snake.move()
    
   
 

screen.exitonclick()
