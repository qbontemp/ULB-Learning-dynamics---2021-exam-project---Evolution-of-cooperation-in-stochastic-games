"""
Generates a graph corresponding to figure 5d of the article
"""

import numpy as np
import matplotlib.pyplot as plt

DSI = []
OG1 = []
OG2 = []
PASTCONSIDER = 500

tot = []
for i in ["DSI","OG1","OG2"]:
    for j in [0.0001, 0.001, 0.01, 0.05, 0.1, 0.5, 1, 10,20,30,40,50,60,70,80,90,100]:
        tot.append(("../dataSaver/MC_MEAN_COOP_initialPopulation_-1_Z_100_beta_{}_mu_0.001_{}_b1_2_b2_1.2_c_1.0_error_0.001_probabilityMoveStayState2_None.npy".format(j,i),j))

DSI = tot[:17]
OG1 = tot[17:34]
OG2 = tot[34:]

x = range(17)  # used to space x-axis ticks evenly

for flist in [(DSI,"DSI"),(OG1,"OG1"),(OG2,"OG2")]:
    toPlotCoop = []
    toPlotProba = []
    for ffile in flist[0]:
        data = np.load(ffile[0])
        toPlotCoop.append(np.mean(data[-PASTCONSIDER:])) # average of the last X numbers
        toPlotProba.append(ffile[1])
    plt.plot(x, toPlotCoop, label=flist[1], marker='o')


plt.xlabel("Selection strength")
plt.xticks(x, [0.0001, 0.001, 0.01, 0.05, 0.1, 0.5, 1, 10,20,30,40,50,60,70,80,90,100], rotation=30)
plt.ylabel("Cooperation rate")
plt.legend()
plt.grid()
plt.savefig("figure5d.png", bbox_inches="tight")
plt.show()
