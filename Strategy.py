"""
Representation and generator for the memory-one strategies used in a two-player prisoner's dilemma
"""
from abc import ABC
import enum
from random import random
from typing import List


class Action(enum.Enum):
    COOP = 0
    DEFECT = 1
    NONE = -1


class State(enum.Enum):
    one = 0
    two = 1

"""
Abstract Strategy class
"""
class Strategy(ABC):

    def play(self, state: State, preceding: list):
        pass

    def getStrategy(self):
        pass

"""
Main implementation of the memory-one strategies
"""
class MemoryOne(Strategy):

    def __init__(self, strategy: str, error: float):
        """
        strategy: list containing 4 bit, each representing the probability to cooperate depending on a situation in the preceding turn.
                  "abcd", a == probability to cooperate if both player cooperated
                          b == probability to cooperate if player1 cooperated and not player2
                          c == probability to cooperate if player2 cooperated and not player1
                          d == probability to cooperate if both player defected
        """
        super().__init__()
        self.error = error
        self.strategy = strategy
        self.computeInit()

    def computeInit(self):
        count = 0
        for proba in self.strategy:
            if (proba == "1"):
                count += 1
        self.probaInit = [count / len(self.strategy), 1 - (count / len(self.strategy))]

    def play(self, state: int, preceding: List[Action]):
        if (preceding[0] == Action.COOP and preceding[1] == Action.COOP):
            action = self.strategy[0]  # 0
        elif (preceding[0] == Action.DEFECT and preceding[1] == Action.COOP):
            action = self.strategy[2]  # 2
        elif (preceding[0] == Action.COOP and preceding[1] == Action.DEFECT):
            action = self.strategy[1]  # 1
        else:
            action = self.strategy[3]  # 3

        if (action == "1"):
            tmp = Action.COOP
        else:
            tmp = Action.DEFECT
        if (random() < self.error):
            if (tmp == Action.COOP):
                tmp = Action.DEFECT
            else:  # DEFECT CASE
                tmp = Action.COOP
        return tmp

    def getFirstTurnProbability(self, action: Action):
        return self.probaInit[action.value]

    def getStrategy(self):
        return self.strategy


"""
Used to generate all 16 possible memory-one strategies for a two-player game
"""
class GeneratorMemoryOne():
    def __init__(self, states=False, error=0):
        """
        states: not used
        error: error rate
        """
        self.error = error
        self.stratList = []
        self.maxLenght = 4
        self.generate("")

    def generate(self, strategy):
        if (len(strategy) < self.maxLength):
            for i in ["1", "0"]:
                st = strategy + i
                self.generate(st)
        else:
            if (not self.states):
                self.stratList.append(MemoryOne(strategy, self.error))
            else:
                self.stratList.append(MemoryOneState(strategy, self.error))

    def getStrategies(self):
        return self.stratList
