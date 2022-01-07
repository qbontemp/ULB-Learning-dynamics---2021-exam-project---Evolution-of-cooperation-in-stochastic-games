"""
Generates a graph corresponding to figure 4 of the article
"""

import numpy as np
import matplotlib.pyplot as plt

PSI = []
PSD = []
PDSD = []
PASTCONSIDER = 500

tot = []
for i in ["PSI","PSD","PDSD"]:
    for j in [0.0001, 0.001, 0.01, 0.05, 0.1, 0.5, 1]:
        tot.append(("../dataSaver/MC_MEAN_COOP_initialPopulation_-1_Z_100_beta_1_mu_0.001_{}_b1_2_b2_1.2_c_1.0_error_0.001_probabilityMoveStayState2_{}.npy".format(i,j),j))
PSI = tot[:7]
PSD = tot[7:14]
PDSD = tot[14:]

x = range(7)  # used to space x-axis ticks evenly

for flist in [(PSI,"PSI"),(PSD,"PSD"),(PDSD,"PSD2")]:
    toPlotCoop = []
    toPlotProba = []
    for ffile in flist[0]:
        data = np.load(ffile[0])
        toPlotCoop.append(np.mean(data[-PASTCONSIDER:])) # average of the last X numbers
        toPlotProba.append(ffile[1])
    plt.plot(x, toPlotCoop, label=flist[1], marker='o')

plt.xlabel("Transition probability")
plt.xticks(x, [0.0001, 0.001, 0.01, 0.05, 0.1, 0.5, 1])
plt.ylabel("Cooperation rate")
plt.legend()
plt.grid()
plt.savefig("figure4.png", bbox_inches="tight")
plt.show()
