import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[5,6,7,8]
#用默认线型和颜色绘制
plt.plot(x,y)
plt.show()
#用蓝色圆圈绘制
plt.plot(x,y,'bo')
plt.show()

y=[1,4,9,16]
#使用x作为索引数组0..N-1绘制y
plt.plot(y)
plt.show()
#使用x作为索引数组0..N-1绘制y,只是颜色为红色，线型为加号
plt.plot(y, 'r+')
plt.show()
