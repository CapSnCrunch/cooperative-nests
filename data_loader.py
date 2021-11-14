import os
import pickle
import numpy as np
import matplotlib.pyplot as plt

save_file = 'nest-4.dat' # Specify which file we want to load

# nest-1 : coexistence
# nest-2 : bistability
# nest-3 *
# nest-4 : cooperative wins
# nest-5 *

data = [] # Data saved as consts, qccounts, qscounts
with open(os.path.dirname(__file__) + '/data/' + save_file, 'rb') as f:
    while True:
        try:
            data.append(pickle.load(f))
        except EOFError:
            break

consts, qccounts, qscounts = data

print(consts)

plt.plot(np.arange(len(qccounts[0])), np.mean(qccounts, axis = 0), label = 'Cooperative')
plt.plot(np.arange(len(qscounts[0])), np.mean(qscounts, axis = 0), label = 'Solitary')
plt.xlabel('Generations')
plt.ylabel('Number of Queens')
plt.legend()
plt.show()

'''fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Ratio of C to S Steady States')
ax.set_xlabel('c1')
ax.set_ylabel('c2')
ax.set_zlabel('c3')
img = ax.scatter(c1vals, c2vals, c3vals, c = np.array(csteadystates) / (np.array(ssteadystates) + 1), cmap = plt.viridis())
fig.colorbar(img)'''

'''ax = fig.add_subplot(122, projection='3d')
ax.set_title('Cooperative Steady States')
ax.set_xlabel('c1')
ax.set_ylabel('c2')
ax.set_zlabel('c3')
img = ax.scatter(c1vals, c2vals, c3vals, c = csteadystates, cmap = plt.viridis())
fig.colorbar(img)'''

plt.show()