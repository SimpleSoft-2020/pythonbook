import turtle
turtle.bgcolor('red')
turtle.fillcolor('yellow')
turtle.pencolor('yellow')
turtle.begin_fill()
sides = 5
length = 300
angle = 720.0 / sides
turtle.penup()
turtle.goto(-400,0)
turtle.pendown()
for i in range(sides):
	turtle.forward(length)
	turtle.right(angle)
turtle.end_fill()
turtle.ht()
turtle.done()