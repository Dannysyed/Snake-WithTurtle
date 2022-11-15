from turtle import Turtle
Starting_position=[(0,0),(-20,0),(-40,0)]
Up=90
Down=270
Left=180
Right=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    
    def create_snake(self):
        for position in Starting_position:
            self.add_segment(position)
         
    def add_segment(self,position):
        new_segment=Turtle('square')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        print(position,'this is position of turtles')
        
    def extend(self):
        # add a new segment
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(20)
    def up(self):
        if self.head.heading()!=Down :
            self.segments[0].setheading(Up)
    def down(self):
       if self.head.heading()!=Up :      
        self.head.setheading(Down)
    def left(self):
      if self.head.heading()!=Right :       
        self.segments[0].setheading(Left)
    def right(self):    
       if self.head.heading()!=Left  :  
        self.segments[0].setheading(Right)
       
        
        
        