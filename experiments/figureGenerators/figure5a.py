"""
Generates a graph corresponding to figure 5a of the article
"""

import numpy as np
import matplotlib.pyplot as plt

DSI = []
OG1 = []
OG2 = []
PASTCONSIDER = 500

tot = []
for i in ["DSI","OG1"]:
    for j in [1,2,3]:
        tot.append(("../dataSaver/MC_MEAN_COOP_initialPopulation_-1_Z_100_beta_1_mu_0.001_{}_b1_{}_b2_1.2_c_1.0_error_0.001_probabilityMoveStayState2_None.npy".format(i,j),j))
DSI = tot[:3]
OG1 = tot[3:]
OG2 = [("../dataSaver/MC_MEAN_COOP_initialPopulation_-1_Z_100_beta_1_mu_0.001_OG2_b1_2_b2_1.2_c_1.0_error_0.001_probabilityMoveStayState2_None.npy",i) for i in [1,2,3]]

for flist in [(DSI,"DSI"),(OG1,"OG1"),(OG2,"OG2")]:
    toPlotCoop = []
    toPlotX = []
    for ffile in flist[0]:
        data = np.load(ffile[0])
        toPlotCoop.append(np.mean(data[-PASTCONSIDER:])) # average of the last X numbers
        toPlotX.append(ffile[1])
    plt.plot(toPlotX, toPlotCoop, label=flist[1], marker='o')

plt.xlabel("Benefit in state 1")
plt.ylabel("Cooperation rate")
plt.legend()
plt.grid()
plt.savefig("figure5a.png", bbox_inches="tight")
plt.show()
