import os
import pickle
import numpy as np
import matplotlib.pyplot as plt

a = 1.0 # ccs / ds     a in [0.5, 2.0]
b = 1.0 # 1 / c3       b in (1.5, 3.0]
c = 2.0 # c1c2 / c3    c in [0.5, 2.0]

# ds = 0.5, rc = 0.5, c1 = 0.99

# coexistence
# 1 1 2, 1 1 3 orange wins
# 2 2 1, 1 2 3  blue wins
# 3 1 1, 3 1 2, 2 1 1, 1 1 1 bistability

for a in [0.8, 0.9, 1.0]:
    for b in [0.8, 0.9, 1.0]:
        for c in [0.8, 0.9, 1.0]:

            save_file = str(a) + ',' + str(b) + ',' + str(c) + '.dat' # Specify which file we want to load

            data = [] # Data saved as consts, qccounts, qscounts
            with open(os.path.dirname(__file__) + '/data5/' + save_file, 'rb') as f:
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

            '''plt.plot(np.arange(len(qccounts[0])), np.mean(qccounts, axis = 0), label = 'Cooperative')
            plt.plot(np.arange(len(qscounts[0])), np.mean(qscounts, axis = 0), label = 'Solitary')
            plt.xlabel('Generations')
            plt.ylabel('Number of Queens')
            plt.legend()
            plt.show()'''

print(results)

plt.hist(qclevels, 10, facecolor = 'blue', alpha = 0.5, label = 'Cooperative')
plt.title('Cooperative Quasi Steady State Distribution')
plt.show()

plt.hist(qslevels, 10, facecolor = 'orange', alpha = 0.5, label = 'Solitary')
plt.title('Solitary Quasi Steady State Distribution')
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