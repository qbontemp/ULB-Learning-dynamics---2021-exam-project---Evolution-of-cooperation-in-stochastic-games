"""
Generates data corresponding to figure 5a of the article
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

b1List = [1,2,3]
for b1 in b1List:
    generateData(INITIAL_POPULATION, Z, BETA, MU, "DSI", ERROR, b1, B2, C, probabilityMoveStayState2)
    generateData(INITIAL_POPULATION, Z, BETA, MU, "OG1", ERROR, b1, B2, C, probabilityMoveStayState2)



generateData(INITIAL_POPULATION, Z, BETA, MU, "OG2", ERROR, B1, B2, C, probabilityMoveStayState2)
