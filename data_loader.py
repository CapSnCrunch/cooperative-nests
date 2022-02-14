import os
import pickle
import numpy as np
from operator import add
import matplotlib.pyplot as plt

a = 1.0 # ccs / ds     a in [0.5, 2.0]
b = 1.0 # 1 / c3       b in (1.5, 3.0]
c = 2.0 # c1c2 / c3    c in [0.5, 2.0]

# ds = 0.5, rc = 0.5, c1 = 0.99

# coexistence
# 1 1 2, 1 1 3 orange wins
# 2 2 1, 1 2 3  blue wins
# 3 1 1, 3 1 2, 2 1 1, 1 1 1 bistability

# data8 is good for 3D charts
# to view proportions, make sure you change constc2, constc3 and labels

c1vals = []
c2vals = []
c3vals = []

coexistence = []
cooperative = []
solitary = []

proportions = {'coexistence' : [], 'cooperative' : [], 'solitary' : []}

constc2 = 0.925
constc3 = 0.975

for a in np.linspace(0.2, 0.4, 5):
    for b in np.linspace(0.8, 1, 5):
        for c in np.linspace(0.4, 0.8, 5):

            save_file = str(round(a, 2)) + ',' + str(round(b, 2)) + ',' + str(round(c, 2)) + '.dat' # Specify which file we want to load

            data = [] # Data saved as consts, qccounts, qscounts
            with open(os.path.dirname(__file__) + '/data-dillon/' + save_file, 'rb') as f:
                while True:
                    try:
                        data.append(pickle.load(f))
                    except EOFError:
                        break

            consts, qccounts, qscounts = data

            qclevels = []
            qslevels = []
            results = {'coexistence': 0, 'cooperative': 0, 'solitary': 0}
            for i in range(len(qccounts)):
                qc_steady_state = np.mean(qccounts[i][-50:])
                qs_steady_state = np.mean(qscounts[i][-50:])

                qclevels.append(qc_steady_state)
                qslevels.append(qs_steady_state)

                if qc_steady_state > 0 and qs_steady_state > 0:
                    results['coexistence'] += 1
                    print('COEXISTENCE', qc_steady_state, qs_steady_state)
                elif qc_steady_state > 0:
                    results['cooperative'] += 1
                else:
                    results['solitary'] += 1

            c1vals.append(consts['c1'])
            c2vals.append(consts['c2'])
            c3vals.append(consts['c3'])
            coexistence.append(results['coexistence'])
            cooperative.append(results['cooperative'])
            solitary.append(results['solitary'])

            print(results)

            if abs(b-constc2) < 0.001 and abs(c-constc3) < 0.001:
                proportions['coexistence'].append(results['coexistence'] / 50)
                proportions['cooperative'].append(results['cooperative'] / 50)
                proportions['solitary'].append(results['solitary'] / 50)

            # plt.plot(np.arange(len(qccounts[0])), np.mean(qccounts, axis = 0), label = 'Cooperative')
            # plt.plot(np.arange(len(qscounts[0])), np.mean(qscounts, axis = 0), label = 'Solitary')
            # plt.xlabel('Generations')
            # plt.ylabel('Number of Queens')
            # plt.legend()
            # plt.show()

print(consts)

# plt.hist(qclevels, 10, facecolor = 'blue', alpha = 0.5, label = 'Cooperative')
# plt.title('Cooperative Quasi Steady State Distribution')
# plt.show()

# plt.hist(qslevels, 10, facecolor = 'orange', alpha = 0.5, label = 'Solitary')
# plt.title('Solitary Quasi Steady State Distribution')
# plt.show()

print(proportions)
labels = ['0.925', '0.95', '0.975', '1.0']
labels = ['1', '2', '3', '4', '5']
width = 0.3
fig, ax = plt.subplots()
ax.bar(labels, proportions['cooperative'], width, label='Cooperative')
ax.bar(labels, proportions['solitary'], width, bottom = proportions['cooperative'], label='Solitary')
ax.bar(labels, proportions['coexistence'], width, bottom = list(map(add, proportions['cooperative'], proportions['solitary'])), label='Coexistence')
ax.set_xlabel('c1')
ax.set_title(f'Proportion of Cases for c2 = {constc2} and c3 = {constc3}')
ax.legend()
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Ratio of Cooperative Outcomes')
ax.set_xlabel('c1')
ax.set_ylabel('c2')
ax.set_zlabel('c3')
img = ax.scatter(c1vals, c2vals, c3vals, c = np.array(cooperative) / 50, cmap = plt.viridis(), vmin = 0, vmax = 1)
fig.colorbar(img)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Ratio of Solitary Outcomes')
ax.set_xlabel('c1')
ax.set_ylabel('c2')
ax.set_zlabel('c3')
img = ax.scatter(c1vals, c2vals, c3vals, c = np.array(solitary) / 50, cmap = plt.viridis(), vmin = 0, vmax = 1)
fig.colorbar(img)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Ratio of Coexistence Outcomes')
ax.set_xlabel('c1')
ax.set_ylabel('c2')
ax.set_zlabel('c3')
img = ax.scatter(c1vals, c2vals, c3vals, c = np.array(coexistence) / 50, cmap = plt.viridis(), vmin = 0, vmax = 1)
fig.colorbar(img)
plt.show()
