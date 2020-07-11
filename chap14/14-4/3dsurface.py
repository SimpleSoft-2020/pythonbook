import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.arange(-10, 10, 0.20)
y = np.arange(-10, 10, 0.20)
x, y = np.meshgrid(x, y)
r = np.sqrt(x**2 + y**2)
z = np.sin(r)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='coolwarm')
plt.show()