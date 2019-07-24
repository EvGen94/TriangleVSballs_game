#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle
import random
import math
import time


# In[ ]:


Wscreen = turtle.Screen()
Wscreen.bgcolor("black")
Wscreen.title("SimpleGame")


# In[ ]:


class Player(turtle.Turtle):
    
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("triangle")
        self.color("white")
        self.speed = 2
       
        
    def move(self):
        self.forward(self.speed)
        
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)
        
    def turnleft(self):
        self.left(20)
    def turnright(self):
        self.right(20)
    def speedup(self):
        self.speed += 1
    def speeddown(self):
        self.speed -= 1
   


# In[ ]:


class Border(turtle.Turtle):
    
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)
        
    def draw_border(self):
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300,-300)
    


# In[ ]:


class Goal(turtle.Turtle):
    
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("green")
        self.shape("circle")
        self.speed = 2
        
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0,360)) #derection 
        
    def jump(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0,360)) #derection     
        
    def move(self):
        self.forward(self.speed)
        
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)     
        


# In[ ]:


class Game(turtle.Turtle):
    
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-290, 310)
        self.score = 0
        
    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), False, align = "left", font=("Arial",14, "normal")) 
         
    def change_score(self, points):
        self.score += points
        self.update_score()


# In[ ]:



player = Player()
border = Border()
game = Game()

border.draw_border()

goals = []
for count in range(10):
    goals.append(Goal())
    

def isCollision(t1, t2):
    a = t1.xcor()-t2.xcor()
    b = t1.ycor()-t2.ycor()
    distance = math.sqrt((a**2)+(b**2))
    
    if distance < 20:
        return True
    else:
        return False 
        

turtle.listen()
turtle.onkey(player.turnleft, "Left")
turtle.onkey(player.turnright, "Right")
turtle.onkey(player.speedup, "Up")
turtle.onkey(player.speeddown, "Down")

Wscreen.tracer(0)

while True:
    Wscreen.update()
    player.move()
       
    for goal in goals:
        goal.move()

        if isCollision(player, goal):
            goal.jump()
            game.change_score(1)
    time.sleep(0.005)
    

