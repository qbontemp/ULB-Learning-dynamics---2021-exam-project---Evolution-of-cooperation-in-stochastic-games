"""
Generates data corresponding to figure 5d of the article
"""

from GLOBAL import generateData

INITIAL_POPULATION = -1
Z = 100
BETA = 1
MU = 0.001
ERROR = 10 ** -3
B1 = 2
B2 = 1.2
C = 1.
probabilityMoveStayState2 = None


betaList = [1,0.5,0.1,0.05,0.01,0.001,0.0001,10,20,30,40,50,60,70,80,90,100]

for beta in betaList:
    generateData(INITIAL_POPULATION, Z, beta, MU, "DSI", ERROR, B1, B2, C, probabilityMoveStayState2)
    generateData(INITIAL_POPULATION, Z, beta, MU, "OG1", ERROR, B1, B2, C, probabilityMoveStayState2)
    generateData(INITIAL_POPULATION, Z, beta, MU, "OG2", ERROR, B1, B2, C, probabilityMoveStayState2)

