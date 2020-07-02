from turtle import *
from random import *

bgpic("bk.png")
for i in range(200):
    pencolor('white')
    penup()
    setx(randint(-300, 300))
    sety(randint(50, 270))
    pendown()
    snow_num = randint(10, 15)
    snow_size = randint(5, 15)
    for j in range(snow_num):
        forward(snow_size)
        backward(snow_size)
        right(360 / snow_num)
ht()
done()