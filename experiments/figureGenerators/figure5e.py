"""
Generates a graph corresponding to figure 5e of the article
"""

import numpy as np
import matplotlib.pyplot as plt

DSI = []
OG1 = []
OG2 = []
PASTCONSIDER = 500

tot = []
for i in ["DSI","OG1","OG2"]:
    for j in [0, 0.0001, 0.001, 0.01, 0.05, 0.1, 0.5, 1]:
        tot.append(("../dataSaver/MC_MEAN_COOP_initialPopulation_-1_Z_100_beta_1_mu_{}_{}_b1_2_b2_1.2_c_1.0_error_0.001_probabilityMoveStayState2_None.npy".format(j,i),j))
DSI = tot[:8]
OG1 = tot[8:16]
OG2 = tot[16:]

x = range(8)  # used to space x-axis ticks evenly

for flist in [(DSI,"DSI"),(OG1,"OG1"),(OG2,"OG2")]:
    toPlotCoop = []
    toPlotProba = []
    for ffile in flist[0]:
        data = np.load(ffile[0])
        toPlotCoop.append(np.mean(data[-PASTCONSIDER:])) # average of the last X numbers
        toPlotProba.append(ffile[1])
    plt.plot(x, toPlotCoop, label=flist[1], marker='o')


plt.xlabel("Mutation rate")
plt.xticks(x, [0, 0.0001, 0.001, 0.01, 0.05, 0.1, 0.5, 1])
plt.ylabel("Cooperation rate")
plt.legend()
plt.grid()
plt.savefig("figure5e.png", bbox_inches="tight")
plt.show()
