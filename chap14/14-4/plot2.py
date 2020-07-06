import matplotlib.pyplot as plt
x=[1,2,3,4,5]
#蓝色 实线 圆圈标记
plt.plot(x,[8,16,24,32,40],'b-o',linewidth=5)
#红色 虚线 正方形标记
plt.plot(x,[1,8,27,64,125],'r--s')
#绿色 虚点线 菱形标记
plt.plot(x,[1,20,12,30,20],'g-.D')
#青绿色 点线 下三角标记
plt.plot(x,[1,90,100,130,120],'c:v')
#黄色 虚线 五边形标记
plt.plot(x,[1,70,50,90,80],'y:p')
plt.show()
