from turtle import *
from random import *

bgpic("bk.png")
for i in range(300):
    pencolor('white')
    penup()
    setx(randint(-400, 400))
    sety(randint(50, 370))
    pendown()
    snow_num = randint(10, 15)
    snow_size = randint(5, 15)
    for j in range(snow_num):
        forward(snow_size)
        backward(snow_size)
        right(360 / snow_num)
ht()
done()