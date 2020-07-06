import numpy as np
import matplotlib.pyplot as plt
N = 100
#x，y数组
x = np.random.rand(N)
y = np.random.rand(N)
#颜色数组
colors = np.random.rand(N)
#散点半径大小
area = np.pi * (15 * np.random.rand(N))**2

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

