import matplotlib.pyplot as plt
import numpy as np
#用来支持中文显示
plt.rcParams['font.sans-serif']=['SimHei','Times New Roman'] 
fig = plt.figure()
#创建一个3D图
ax = fig.gca(projection='3d')
ax.set_title("3D散点图")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
N = 100
#x，y数组
x = np.random.rand(N)
y = np.random.rand(N)
z = np.random.rand(N)
#颜色数组
colors = np.random.rand(N)
#散点半径大小
area = np.pi * (15 * np.random.rand(N))**2
ax.scatter(x, y, s=area, c=colors, alpha=0.5)
ax.scatter(y, z, s=area, c=colors, alpha=0.5)
ax.scatter(x, z, s=area, c=colors, alpha=0.5)
plt.show()

