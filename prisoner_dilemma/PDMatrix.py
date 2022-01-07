"""
PDMatrix = Prisoner's dilemma reward matrix
"""

class PDMatrix:

    def __init__(self, b: float, c: float) ->  None:
        self.b = b
        self.c = c
        self.matrix = [[b-c,-c],[b,0]]

    def getPayoff(self, player1: int, player2: int):
        """
        get payoff of two action 
        :param player1: action of player 1 in matrix
        :param player2: action of player 2 in matrix
        :return:
        """
        return self.matrix[player1][player2]
