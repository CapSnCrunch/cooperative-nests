import os
import pickle
import numpy as np
import matplotlib.pyplot as plt

a = 3.0 # ccs / ds     a in [0.5, 2.0]
b = 1.0 # 1 / c3       b in (1.5, 3.0]
c = 2.0 # c1c2 / c3    c in [0.5, 2.0]

# ds = 0.5, rc = 0.5, c1 = 0.99

# coexistence
# 1 1 2, 1 1 3 orange wins
# 2 2 1, 1 2 3  blue wins
# 3 1 1, 3 1 2, 2 1 1, 1 1 1 bistability

#for a in np.linspace(1, 3, 3):
#    for b in np.linspace(1, 3, 3):
#        for c in np.linspace(1, 3, 3):

save_file = str(a) + ',' + str(b) + ',' + str(c) + '.dat' # Specify which file we want to load
print(save_file)

data = [] # Data saved as consts, qccounts, qscounts
with open(os.path.dirname(__file__) + '/data/' + save_file, 'rb') as f:
    while True:
        try:
            data.append(pickle.load(f))
        except EOFError:
            break

consts, qccounts, qscounts = data

print(consts)

qclevels = []
qslevels = []
for i in range(len(qccounts)):
    qclevels.append(np.mean(qccounts[i][-50:]))
    qslevels.append(np.mean(qscounts[i][-50:]))

plt.plot(np.arange(len(qccounts[0])), np.mean(qccounts, axis = 0), label = 'Cooperative')
plt.plot(np.arange(len(qscounts[0])), np.mean(qscounts, axis = 0), label = 'Solitary')
plt.xlabel('Generations')
plt.ylabel('Number of Queens')
plt.legend()
plt.show()

#plt.scatter(qclevels, np.arange(50), label = 'Cooperative')
#plt.scatter(qslevels, np.arange(50), label = 'Solitary')
#plt.show()

'''plt.hist(qclevels, 10, facecolor = 'blue', alpha = 0.5, label = 'Cooperative')
plt.title('Cooperative Quasi Steady State Distribution')
plt.show()

plt.hist(qslevels, 10, facecolor = 'orange', alpha = 0.5, label = 'Solitary')
plt.title('Solitary Quasi Steady State Distribution')
plt.show()'''

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