"""
Generates a graph corresponding to the condensed figure 2 of the article
"""
import matplotlib.pyplot as plt
import numpy as np

PATH_TO_OG1 = "../dataSaver/MC_MEAN_COOP_initialPopulation_-1_Z_100_beta_1_mu_0.001_OG1_b1_2_b2_1.2_c_1.0_error_0.001_probabilityMoveStayState2_None.npy"
PATH_TO_OG2 = "../dataSaver/MC_MEAN_COOP_initialPopulation_-1_Z_100_beta_1_mu_0.001_OG1_b1_2_b2_1.2_c_1.0_error_0.001_probabilityMoveStayState2_None.npy"
PATH_TO_DSI = "../dataSaver/MC_MEAN_COOP_initialPopulation_-1_Z_100_beta_1_mu_0.001_DSI_b1_2_b2_1.2_c_1.0_error_0.001_probabilityMoveStayState2_None.npy"
PATH_TO_DSD = "../dataSaver/MC_MEAN_COOP_initialPopulation_-1_Z_100_beta_1_mu_0.001_DSD_b1_2_b2_1.2_c_1.0_error_0.001_probabilityMoveStayState2_None.npy"
PATH_TO_PSI = "../dataSaver/MC_MEAN_COOP_initialPopulation_-1_Z_100_beta_1_mu_0.001_PSI_b1_2_b2_1.2_c_1.0_error_0.001_probabilityMoveStayState2_0.5.npy"
PATH_TO_PSD = "../dataSaver/MC_MEAN_COOP_initialPopulation_-1_Z_100_beta_1_mu_0.001_PSD_b1_2_b2_1.2_c_1.0_error_0.001_probabilityMoveStayState2_0.5.npy"
PATH_TO_PSD2 = "../dataSaver/MC_MEAN_COOP_initialPopulation_-1_Z_100_beta_1_mu_0.001_PDSD_b1_2_b2_1.2_c_1.0_error_0.001_probabilityMoveStayState2_0.5.npy"

list_files = [PATH_TO_OG1, PATH_TO_OG2, PATH_TO_DSI, PATH_TO_DSD, PATH_TO_PSI, PATH_TO_PSD, PATH_TO_PSD2]
list_names = ["OG1","OG2","DSI","DSD","PSI","PSD","PSD2"]

for i in range(len(list_names)):
    data = np.load(list_files[i])
    plt.plot(range(data.shape[0]), data, label=list_names[i])

plt.xlabel("Time steps")
plt.ylabel("Cooperation rate")
plt.legend()
plt.grid()
plt.savefig("figure2.png", bbox_inches="tight")
plt.show()
