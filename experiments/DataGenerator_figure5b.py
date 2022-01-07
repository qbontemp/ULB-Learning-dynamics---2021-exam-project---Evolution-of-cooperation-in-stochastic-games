"""
Generates data corresponding to figure 5b of the article
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

b2List = [1,2,3]
for b2 in b2List:
    generateData(INITIAL_POPULATION, Z, BETA, MU, "DSI", ERROR, B1, b2, C, probabilityMoveStayState2)
    generateData(INITIAL_POPULATION, Z, BETA, MU, "OG2", ERROR, B1, b2, C, probabilityMoveStayState2)


generateData(INITIAL_POPULATION, Z, BETA, MU, "OG1", ERROR, B1, B2, C, probabilityMoveStayState2)
