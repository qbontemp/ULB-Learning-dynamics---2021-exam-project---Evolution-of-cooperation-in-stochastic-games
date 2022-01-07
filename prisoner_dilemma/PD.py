""""
Prisoner's dilemma generic class
"""

from abc import ABC, abstractmethod
import numpy as np
from typing import List
from Strategy import Strategy, Action, State


class PD(ABC):
    def __init__(self,startingPrecedingList : List[List[Action]], strategies: List[Strategy], nbRounds: int, levelMeanOfPayoff = 1000 ):
        self.nbRounds = nbRounds
        self.strategies = strategies
        self.payoffs = [[0] * len(self.strategies) for i in range(len(self.strategies))] # Matrix payoff size S x S where S is a strategy, dans payoff[S1][S2] is the average payoff of strategie 1 when play against strategie 2
        self.cooperationRates = [[0] * len(self.strategies) for i in range(len(self.strategies))] # Matrix cooperationRates size S x S where S is a strategy, dans cooperationRates[S1][S2] is the average cooperation Rates of strategie 1 when play against strategie 2
        self.state = State.one
        self.levelOfMean = levelMeanOfPayoff   # how many iterations are averaged in the end
        self.startListPreceding = startingPrecedingList

    def compute(self) -> None:
        """
        Computes a static payoff and cooperation matrix for each stategy
        """
        for cmpt in range(1,self.levelOfMean+1): # the iterations are averaged later
            for player1 in range(len(self.strategies)):
                for player2 in range(len(self.strategies)):
                    payoff_average = 0
                    coopCount_average = 0
                    for preceding in self.startListPreceding:  # simulates previous actions on the first round
                        initial = [preceding[0], preceding[1]]
                        payoff = 0
                        coopCount = 0
                        for round in range(self.nbRounds):
                            payoff += self._computePayoff(preceding)
                            if (preceding[0] == Action.COOP):
                                coopCount += 1

                            self._changeState(preceding)

                            preceding = self._makePlayerPlay(player1, player2, preceding)

                        payoff_average += payoff * self.strategies[player1].getFirstTurnProbability(initial[0]) * self.strategies[player2].getFirstTurnProbability(initial[1])
                        coopCount_average += coopCount * self.strategies[player1].getFirstTurnProbability(initial[0]) * self.strategies[player2].getFirstTurnProbability(initial[1])

                    # calculate payoff and cooperation rate
                    self.payoffs[player1][player2] = self.payoffs[player1][player2] + (1/cmpt) * (payoff_average - self.payoffs[player1][player2]) #Q^ = 1/k sum(Ri) ===> Assignement 3 mean calculation
                    coop_mean = coopCount_average / self.nbRounds
                    self.cooperationRates[player1][player2] = self.cooperationRates[player1][player2] + (1/cmpt) * (coop_mean - self.cooperationRates[player1][player2])


            if(cmpt%100 == 0):
                print(cmpt/(self.levelOfMean) *100,"%")

    @abstractmethod
    def _changeState(self, preceding: List[Action]) -> None:
        """
        Describes how the game changes state
        :param preceding: list of actions of player 1 and player 2
        """
        pass

    @abstractmethod
    def _computePayoff(self, preceding: List[Action]) -> float:
        """
        Computes the payoff of the player 1
        :param preceding: list of the actions made of the previous round
        :return: the value of payoff of player 1
        """
        pass


    def _makePlayerPlay(self, player1: int, player2: int, preceding: List[Action]) -> List[Action]:
        """
        Makes the two players play against each other

        :param player1:
        :param player2:
        :param preceding: list of actions of player one and player two
        :return: list of new play action of player one and player two
        """
        tmp = []
        tmp.append(self.strategies[player1].play(self.state, preceding))
        tmp.append(self.strategies[player2].play(self.state, preceding))
        return tmp

    def getPayoffs(self) -> np.array:
        ret = np.array(self.payoffs)
        ret = ret / np.amax(np.absolute(ret))
        return ret

    def getCooperationRate(self) -> np.array:
        return np.array(self.cooperationRates)
