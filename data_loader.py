import os
import pickle
import numpy as np
import matplotlib.pyplot as plt

save_file = 'steady_states_5.dat' # Specify which files we want to load

data = [] # Data saved as c1vals, c2vals, c3vals, ssteadystates, csteadystates
with open(os.path.dirname(__file__) + '/data/' + save_file, 'rb') as f:
    while True:
        try:
            data.append(pickle.load(f))
        except EOFError:
            break

c1vals, c2vals, c3vals, ssteadystates, csteadystates = data

fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
ax.set_title('Solitary Steady States')
ax.set_xlabel('c1')
ax.set_ylabel('c2')
ax.set_zlabel('c3')
img = ax.scatter(c1vals, c2vals, c3vals, c = ssteadystates, cmap = plt.viridis())
fig.colorbar(img)

ax = fig.add_subplot(122, projection='3d')
ax.set_title('Cooperative Steady States')
ax.set_xlabel('c1')
ax.set_ylabel('c2')
ax.set_zlabel('c3')
img = ax.scatter(c1vals, c2vals, c3vals, c = csteadystates, cmap = plt.viridis())
fig.colorbar(img)

plt.show()