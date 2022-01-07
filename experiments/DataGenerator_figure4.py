"""
Generates data corresponding to figure 4 of the article
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

probabilityToMoveStayState2List = [1, 0.5, 0.1, 0.05, 0.01, 0.001, 0.0001]
for probabilityMoveStayState2 in probabilityToMoveStayState2List:
    generateData(INITIAL_POPULATION, Z, BETA, MU, "PSI", ERROR, B1, B2, C, probabilityMoveStayState2)
    generateData(INITIAL_POPULATION, Z, BETA, MU, "PSD", ERROR, B1, B2, C, probabilityMoveStayState2)
    generateData(INITIAL_POPULATION, Z, BETA, MU, "PDSD", ERROR, B1, B2, C, probabilityMoveStayState2)

