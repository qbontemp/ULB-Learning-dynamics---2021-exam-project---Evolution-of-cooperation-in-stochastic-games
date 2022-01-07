"""
Generates data corresponding to figure 2 of the article
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

generateData(INITIAL_POPULATION, Z, BETA, MU, "DSD", ERROR, B1, B2, C, probabilityMoveStayState2)
generateData(INITIAL_POPULATION, Z, BETA, MU, "DSI", ERROR, B1, B2, C, probabilityMoveStayState2)
generateData(INITIAL_POPULATION, Z, BETA, MU, "OG1", ERROR, B1, B2, C, probabilityMoveStayState2)
generateData(INITIAL_POPULATION, Z, BETA, MU, "OG2", ERROR, B1, B2, C, probabilityMoveStayState2)

probabilityMoveStayState2 = 0.5

generateData(INITIAL_POPULATION, Z, BETA, MU, "PSI", ERROR, B1, B2, C, probabilityMoveStayState2)
generateData(INITIAL_POPULATION, Z, BETA, MU, "PSD", ERROR, B1, B2, C, probabilityMoveStayState2)
generateData(INITIAL_POPULATION, Z, BETA, MU, "PDSD", ERROR, B1, B2, C, probabilityMoveStayState2)
