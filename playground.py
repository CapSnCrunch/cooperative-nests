import numpy as np

rc = 20
ds = 0.6
ccs = 1
a = ccs / ds

results = [0, 0, 0, 0] # coexistence, bistability, solitary, cooperative

for c1 in np.linspace(0.8, 1, 5):
    print(c1)
    for c2 in np.linspace(0.8, 1, 5):
        for c3 in np.linspace(0.8, 1, 5):
            b = 1 / c3
            c = c1 * c2 / c3
            if a < min(b, c):
                results[0] += 1
            elif a > max(b, c):
                results[1] += 1
            elif b < a < c:
                results[2] += 1
            elif c < a < b:
                results[3] += 1

print(results)