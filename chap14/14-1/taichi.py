import turtle
turtle.pencolor('red')
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(200,180)
turtle.circle(100,180)
turtle.circle(-100,180)
turtle.end_fill()

turtle.pencolor('blue')
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.circle(-100)
turtle.circle(-200,180)
turtle.seth(180)
turtle.circle(100,180)
turtle.end_fill()

turtle.penup()
turtle.pencolor('white')
turtle.fillcolor('white')
turtle.begin_fill()
turtle.sety(60)
turtle.circle(40)
turtle.end_fill()

turtle.pencolor('black')
turtle.fillcolor('black')
turtle.begin_fill()
turtle.sety(260)
turtle.circle(40)
turtle.end_fill()
turtle.ht()

turtle.done()