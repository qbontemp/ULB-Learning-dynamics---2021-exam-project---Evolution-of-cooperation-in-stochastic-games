"""
Single-state prisoner's dilemma
"""

from typing import List
from Strategy import Strategy, Action
from prisoner_dilemma.PDMatrix import PDMatrix
from prisoner_dilemma.PD import PD


class OnlyOneGame(PD):
    
    def __init__(self,startingPrecedingList : List[List[Action]], strategies: List[Strategy], nbRounds: int, b: float, c: float) ->  None:
        super().__init__(startingPrecedingList,strategies, nbRounds)
        self.b = b
        self.c = c
        self.PDMatrix = PDMatrix(b, c)
        self.compute()

    def _changeState(self, preceding: List[Action]) -> None:
        """
        Describes how the game changes state
        :param preceding: list of action of player 1 and player 2
        """
        pass #NOTHING


    def _computePayoff(self, preceding: List[Action]) -> float:
        """
        Computes the payoff of player 1
        :param preceding: list of the two actions made by the players on the previous round
        :return: the payoff of player 1
        """
        return self.PDMatrix.getPayoff(preceding[0].value, preceding[1].value)
