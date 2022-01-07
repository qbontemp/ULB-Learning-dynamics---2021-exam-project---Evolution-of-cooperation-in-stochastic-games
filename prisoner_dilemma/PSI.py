""""
Probabilistic state-independent prisoner's dilemma
"""

import random

from typing import List
from Strategy import Strategy,Action,State
from prisoner_dilemma.PDMatrix import PDMatrix
from prisoner_dilemma.PD import PD


class PSI(PD):
    def __init__(self,startingPrecedingList : List[List[Action]], strategies: List[Strategy], nbRounds: int, b1: float, b2: float, c: float,
                 probabilityToMoveState2: float) -> None:
        super().__init__(startingPrecedingList,strategies, nbRounds)
        self.b1 = b1
        self.b2 = b2
        self.c = c
        self.goState2 = probabilityToMoveState2
        self.PDMatrix1 = PDMatrix(b1, c)
        self.PDMatrix2 = PDMatrix(b2, c)
        self.compute()

    def _changeState(self, preceding: List[Action]) -> None:
        """
        Describes how the game changes state
        :param preceding: list of actions of player 1 and player 2
        """
        if (self.state == State.one):
            if (preceding[0] == Action.COOP and preceding[1] == Action.COOP):
                if (random.random() < self.goState2):
                    self.state = State.two
            else: #Someone has defect
                self.state = State.two
        else:#STATE  2
            if (preceding[0] == Action.COOP and preceding[1] == Action.COOP):
                if (random.random() < (1- self.goState2)):
                    self.state = State.one

    def _computePayoff(self, preceding: List[Action]) -> float:
        """
        Computes the payoff of player 1
        :param preceding: list of the actions made of the previous round
        :return: the value of payoff of player 1
        """
        if (self.state == State.one):
            return self.PDMatrix1.getPayoff(preceding[0].value, preceding[1].value)
        else:
            return self.PDMatrix2.getPayoff(preceding[0].value, preceding[1].value)
