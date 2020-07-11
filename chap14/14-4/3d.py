import matplotlib.pyplot as plt
#用来支持中文显示
plt.rcParams['font.sans-serif']=['SimHei','Times New Roman'] 
fig = plt.figure()
#创建一个3D图
ax = fig.gca(projection='3d')
x=[1,2,6,4,5]
y=[6,7,8,12,10]
z=[11,12,13,14,19]
ax.set_title("3D折线")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.plot(x, y, z, c='b')
plt.show()
