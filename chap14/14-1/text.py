import turtle 
from random import *
turtle.bgcolor("white") 
text="Python Turtle"
colors=['black','red','yellow','purple','blue','green'] 
for pos in range(50): 
	turtle.pencolor(colors[randint(0,5)]) 
	turtle.penup() 
	turtle.forward(pos*5) 
	turtle.pendown() 
	turtle.write(text,font=("Arial",pos+10)) 
	turtle.left(30) 
turtle.ht()
turtle.done() 
