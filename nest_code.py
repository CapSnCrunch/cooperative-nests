import os
import pickle
import pygame
import numpy as np
from os.path import exists
import matplotlib.pyplot as plt

# TODO Update Overleaf
# TODO Presentation on effects of ci on dynamics (show average steady states as a function of c1, c2, c3)
# Ratio on the whole landscape
# Ratio in inidividual colonies

c1 = 1 # Ratio of mortality rates (dc / ds) (used in queen fights)
ds = 0.6 # Mortality rate of solitary queens
c2 = 0.1 # Ratio of interspecific competition ability (csc / ccs) (used in cluster fights)
ccs = 0.8 # Interspecific competition ability of cooperative queens
c3 = 1 # Ratio of reproductive capabilities (rs / rc) (used in reproduction)
rc = 0.8 # Reproductive ability of cooperative queens
sigma = 1 # Reproductive variance (sigma^2) (used in reproduction)

K = 25
m, n = 5, 5
qc0, qs0 = 50, 50

# Wrap constants into a dictionary
consts = {'c1':c1, 'ds':ds, 'c2':c2, 'ccs':ccs, 'c3':c3, 'rc':rc, 'sigma':sigma}
print('consts', consts)
print('ccs / ds:', ccs / ds)
print('1 / c3:', 1 / c3)
print('c1c2 / c3:', c1*c2 / c3)

sims = 50 # Number of simulations to run and average
gens = 500 # Number of generations to simulate

datanum = 0
#save_file = 'nest-' + str(datanum) # Specify where we want to save the data

class Cluster():
    def __init__(self, i, j, consts):
        self.i = i
        self.j = j
        self.qc = 0 # Number of cooperative queens
        self.qs = 0 # Number of solitary queens
        self.consts = consts

    def potential(self):
        xi = self.qs * (self.consts['c2'] * self.consts['ccs']) * (1 - self.consts['ds'])
        xi += self.qc * (self.consts['ccs']) * (1 - self.consts['ds'] * self.consts['c1'])
        return -2.88 + 4.28 * xi - 0.377 * (xi ** 2)

    def queen_fight(self, Cm = 5):
        while (self.qc + self.qs) >= Cm:
            self.qc = int(self.qc * (1 - self.consts['ds'] * self.consts['c1']))
            self.qs = int(self.qs * (1 - self.consts['ds']))

class Landscape():
    def __init__(self, K, m, n, consts):
        '''K: size of individual clusters (int)
           m x n: size of grid of clusters (int) (int)
           p: probability a queen is cooperative (double 0-1)
           consts: dictionary of c1, c2, c3, ds, rc, ccs, and sigma'''
        self.K = K
        self.m = m
        self.n = n
        self.consts = consts
        self.clusters = []
        for i in range(m):
            new_row = []
            for j in range(n):
                new_row.append(Cluster(i, j, self.consts))
            self.clusters.append(new_row)

    def create_queens(self, qc = 0, qs = 0):
        '''Q: number of queens to populate the grid with (int)
            qc: a specific number of cooperative queens to include
            qs: a specific number of solitary queens to include'''

        # TODO RESTRICT INITIAL NUMBER OF QUEENS IN EACH CLUSTER TO ...

        locations = [x for x in range(self.K * self.K * self.m * self.n)]
        types = [0 for x in range(qc)] + [1 for x in range(qs)]
        np.random.shuffle(types)
        while len(types) > 0:
            new_position = locations.pop(np.random.randint(len(locations))) // (self.K * self.K)
            cluster = self.clusters[new_position // self.n][new_position % self.n]
            if types.pop() == 1:
                cluster.qs += 1
                qs -= 1
            else:
                cluster.qc += 1
                qc -= 1

    def queen_count(self):
        '''Count the number of P (cooperative) and H (solitary) queens on the whole landscape'''
        qc, qs = 0, 0
        for row in self.clusters:
            for cluster in row:
                qc += cluster.qc
                qs += cluster.qs
        return (qc, qs)

    def queen_fight(self):
        '''Simulate fights between queens within the clusters'''
        for row in self.clusters:
            for cluster in row:
                cluster.queen_fight()

    def cluster_fight(self):
        '''Simulate fights between all neighboring clusters'''

        dead_colonies = []
        for i in range(self.m):
            for j in range(self.n):
                # Calculate total potential of all neighbors in Von Neumann neighborhood
                total_potential = 0
                for (x,y) in [(0,-1), (1,0), (0,1), (-1, 0)]:
                    if 0 <= i+x < self.m and 0 <= j+y < self.n:
                        total_potential += max(0, self.clusters[i+x][j+y].potential())
                if total_potential != 0:
                    if np.random.uniform() > self.clusters[i][j].potential() / total_potential:
                        dead_colonies.append(self.clusters[i][j])
        
        for colony in dead_colonies:
            colony.qc = 0
            colony.qs = 0
        
    def reproduce(self):
        QC, QS = 0, 0
        for row in self.clusters:
            for cluster in row:
                while cluster.qc > 0:
                    QC += max(0, np.random.normal(50 * self.consts['rc'], self.consts['sigma']))
                    cluster.qc -= 1
                while cluster.qs > 0:
                    QS += max(0, np.random.normal(50 * self.consts['rc'] * self.consts['c3'], self.consts['sigma']))
                    cluster.qs -= 1
        #print(QC, QS)
        self.create_queens(qc = int(QC), qs = int(QS))

def gather_data(consts, savefile):

    qc_count_average = []
    qs_count_average = []

    for i in range(sims):
        #if i % 10 == 0:
        #    print('Simulation', i)
        print('Simulation', i)
        land = Landscape(K = K, m = m, n = n, consts = consts)
        land.create_queens(qc = qc0, qs = qs0)

        qc_counts = []
        qs_counts = []

        for j in range(gens):
            # Record queen counts for i-th generation
            qc, qs = land.queen_count()
            qc_counts.append(qc)
            qs_counts.append(qs)

            # Simulate i-th generation
            land.queen_fight()
            land.cluster_fight()
            land.reproduce()
        
        qc_count_average.append(np.array(qc_counts))
        qs_count_average.append(np.array(qs_counts))

    with open(os.path.dirname(__file__) + '/auto-data2/' + savefile + '.dat', 'wb') as f:
        pickle.dump(consts, f)
        pickle.dump(qc_count_average, f)
        pickle.dump(qs_count_average, f)

if __name__ == '__main__':

    ################# SIGNLE STEP SIMULATION #################
    run = False

    scale = 100
    if run:
        win = pygame.display.set_mode((m * scale + 2, int((n + 0.5) * scale + 2)))
        pygame.display.set_caption('Ant Nest Simulator')
        pygame.font.init()
        font = pygame.font.SysFont('Calibri', int(scale / 5))

    land = Landscape(K = K, m = m, n = n, consts = consts)
    land.create_queens(qc = qc0, qs = qs0)

    with_cluster_fights = True
    step = 0 # 0: queen fight, 1: cluster fight, 2: reproduce

    generation = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if with_cluster_fights:
                    if step == 0:
                        land.queen_fight()
                    elif step == 1:
                        land.cluster_fight()
                    else:
                        land.reproduce()
                        generation += 1
                    step = (step + 1) % 3
                else:
                    if step == 0:
                        land.queen_fight()
                    else:
                        land.reproduce()
                        generation += 1
                    step = (step + 1) % 2

        win.fill((255, 255, 255))

        # Draw grid lines
        for i in range(m + 1):
            pygame.draw.line(win, (0,0,0), (i*scale, 0), (i*scale, m*scale), 2)
        for i in range(n + 1):
            pygame.draw.line(win, (0,0,0), (0, i*scale), (n*scale, i*scale), 2)
        
        # Display qc and qs for each cluster
        for i in range(m):
            for j in range(n):
                qc = land.clusters[i][j].qc
                qs = land.clusters[i][j].qs
                if qc + qs > 0:
                    win.blit(font.render('qc: ' + str(qc), False, (249, 115, 6)), ((i+0.3)*scale, (j+0.3)*scale))
                    win.blit(font.render('qs: ' + str(qs), False, (3, 67, 223)), ((i+0.3)*scale, (j+0.5)*scale))

        win.blit(font.render('Generation: ' + str(generation), False, (0, 0, 0)), ((0.2)*scale, (n+0.2)*scale))
        if with_cluster_fights:
            win.blit(font.render('Next Event: ' + ['Queen Fight', 'Cluster Fight', 'Reproduction'][step], False, (0, 0, 0)), (1.5*scale, (n+0.2)*scale))
        else:
            win.blit(font.render('Next Event: ' + ['Queen Fight', 'Reproduction'][step], False, (0, 0, 0)), (1.5*scale, (n+0.2)*scale))
        win.blit(font.render('Q: ' + str(land.queen_count()), False, (0, 0, 0)), (3.7*scale, (n+0.2)*scale))
        pygame.display.update()

    ################# GATHER 3D DATA #################
    # ~2min per simulations
    for a in np.linspace(0.5, 2, 4):
        for b in np.linspace(1.5, 3, 4):
            for c in np.linspace(0.5, 2, 4):

                print()
                consts = {'c1':0.99, 'ds':0.5, 'c2':c/(0.99*b), 'ccs':0.5*a, 'c3':1/b, 'rc':0.5, 'sigma':1}

                '''savefile = ''
                vals = [consts[c] for c in list(consts.keys())]
                for i in range(len(vals)):
                    savefile += str(vals[i])
                    if i < len(vals) - 1:
                        savefile += ","'''

                '''datanum = 0
                while exists(os.path.dirname(__file__) + '/data/' + savefile):
                    datanum += 1
                savefile += '-' + str(datanum)'''
                
                try:
                    savefile = str(a)[:3] + ',' + str(b)[:3] + ',' + str(c)[:3]
                    print('SAVEFILE', savefile)
                    print('CONSTANTS', consts)
                    gather_data(consts, savefile)
                except:
                    print("ERROR")
                    with open(os.path.dirname(__file__) + '/auto-data2/error-log.txt', 'w') as f:
                        f.write(savefile + '\n')
                        f.write(str(consts) + '\n')
                        f.write('\n')