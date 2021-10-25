from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Normal Curves')

x = np.random.standard_normal(100)
y = np.random.standard_normal(100)
z = np.random.standard_normal(100)
c = np.random.standard_normal(100)

img = ax.scatter(x, y, z, c = c, cmap=plt.hot())
ax.set_xlabel('c1')
ax.set_ylabel('c2')
ax.set_zlabel('c3')
fig.colorbar(img)
plt.show()