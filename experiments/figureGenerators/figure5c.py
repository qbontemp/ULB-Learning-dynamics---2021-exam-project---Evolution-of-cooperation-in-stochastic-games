"""
Generates a graph corresponding to figure 5c of the article
"""

import numpy as np
import matplotlib.pyplot as plt

DSI = []
OG1 = []
OG2 = []
PASTCONSIDER = 500

tot = []
for i in ["DSI","OG1","OG2"]:
    for j in [0.0001, 0.001, 0.01, 0.05, 0.1, 0.5, 1]:
        tot.append(("../dataSaver/MC_MEAN_COOP_initialPopulation_-1_Z_100_beta_1_mu_0.001_{}_b1_2_b2_1.2_c_1.0_error_{}_probabilityMoveStayState2_None.npy".format(i,j),j))


DSI = tot[:7]
OG1 = tot[7:14]
OG2 = tot[14:]

x = range(7)  # used to space x-axis ticks evenly

for flist in [(DSI,"DSI"),(OG1,"OG1"),(OG2,"OG2")]:
    toPlotCoop = []
    toPlotProba = []
    for ffile in flist[0]:
        data = np.load(ffile[0])
        toPlotCoop.append(np.mean(data[-PASTCONSIDER:])) # average of the last X numbers
        toPlotProba.append(ffile[1])
    plt.plot(x, toPlotCoop, label=flist[1], marker='o')

plt.xlabel("Error rate")
plt.xticks(x, [0.0001, 0.001, 0.01, 0.05, 0.1, 0.5, 1])
plt.ylabel("Cooperation rate")
plt.legend()
plt.grid()
plt.savefig("figure5c.png", bbox_inches="tight")
plt.show()
