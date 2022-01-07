"""
Implementation of the Monte Carlo simulation for a two-player stochastic prisoner's dilemma and the two deterministic sub-games.
"""
import copy
from math import e
import numpy as np

NUMBER_POP_SAVE = 1000


class MonteCarlo:

    def __init__(self, Z: int, beta: float, mu: float, A: np.array, C: np.array, initalPopulationStrategy : int = -1):
        """
        :param Z: population size
        :param beta: selection strength
        :param mu: mutation probability
        :param A: payoff matrix
        :param C: cooperation matrix
        :param initialPopulation: value between 0 and 15 (included) representing the initial population strategies
        """
        self.Z = Z
        self.beta = beta
        self.mu = mu
        self.A = A
        self.C = C
        self.coopResults = None
        self.errorResults = None
        self.initalPopulationStrategy = initalPopulationStrategy

    def simulate(self, nbStep: int, nbInit: int, nbRun: int):
        """
        :param nbStep: number of time steps to simulate
        :param nbInit: number of preliminary steps to simulate (before counting data)
        :param nbRun: number of times the simulation is run (to take the average)
        """
        self.nbStep = nbStep
        coopInterResults = np.zeros((0,nbStep))
        self.ListLast1000EvolutionOfPopulationForEveryRun = []
        for run in range(nbRun):
            ListOfLast1000EvolutionOfPopulation = []
            print("Starting run {} of {}.".format(run+1, nbRun))
            popInit = np.random.randint(0,high=len(self.A),size=(1,self.Z))

            if(self.initalPopulationStrategy != -1):
                for person in range(len(popInit[0])):
                    popInit[0][person] = self.initalPopulationStrategy

            coopRe = np.zeros((1,nbStep))
            self.pop = {}  #dictionary : {key=strategie : value=nb using this strategy in the pop}
            for strategy in range(len(self.A)):
                self.pop[strategy] = np.count_nonzero(popInit == strategy)
            for init in range(nbInit): #training part
                self._moran_step()
            for step in range(nbStep): #testing part
                self._moran_step()
                if (step >= nbStep - NUMBER_POP_SAVE):
                    ListOfLast1000EvolutionOfPopulation.append(copy.deepcopy(self.pop))
                coopRe[0,step] = self._computeCoopRate()

            self.ListLast1000EvolutionOfPopulationForEveryRun.append(ListOfLast1000EvolutionOfPopulation)
            coopInterResults = np.append(coopInterResults, coopRe, axis=0)
        self.coopResults = np.mean(coopInterResults, axis=0)
        self.errorResults = np.std(coopInterResults, axis=0)

        
    def _moran_step(self):
        """
        Moran step implementation
        Selects two players randomly, makes them compete against all other players, then, following a probability, either mutates their strategy into another one, or makes them imitate the other player's strategy if it is better performing
        """
        state_list = [] # list of [strategy] * nb using the strat, like [strat1, strat1, strat2] for 3 players
        for strategy in self.pop:
            state_list = state_list + [strategy]*self.pop[strategy]
        selection = np.random.choice(state_list,size=2,replace=False) # selects two players for the moran step
        prem_fit = self._fitness(selection[0])
        second_fit = self._fitness(selection[1])
        proba_imit = (1+e**(self.beta*(prem_fit - second_fit)))**(-1)
        if(np.random.rand() < self.mu):  # mutation event
            self.pop[np.random.randint(0,high=len(self.A))] += 1
            self.pop[selection[0]] -= 1
        elif(np.random.rand() < proba_imit): # imitation event
            self.pop[selection[1]] += 1
            self.pop[selection[0]] -= 1

    def _fitness(self, currentStrategy: int):
        """
        Computes the fitness of a strategy
        :param currentStrategy: strategy
        :return: fitness of strategy
        """
        fitness = 0
        for strategy in self.pop:
            if (strategy != currentStrategy):
                fitness += self.pop[strategy]*self.A[currentStrategy,strategy]
            else:
                fitness += (self.pop[strategy]-1)*self.A[currentStrategy,strategy] # do not play against himself
        return fitness/(self.Z-1)

    def _computeCoopRate(self):
        """
        Computes cooperation rate at the current time step
        :return: cooperation rate
        """
        coopRate = 0
        for strategy1 in range(len(self.A)):
            for strategy2 in range(strategy1,len(self.A)):
                if(strategy1 == strategy2): # nbStrat1% * nbStrat2% * avgCoopRate[strat1 agst strat2]
                    coopRate += (self.pop[strategy1]/self.Z)*((self.pop[strategy2]-1)/(self.Z-1))*self.C[strategy1,strategy2] # play against same strategy
                else:
                    coopRate += (self.pop[strategy1]/self.Z)*(self.pop[strategy2]/(self.Z-1))*((self.C[strategy1,strategy2] + self.C[strategy2,strategy1])/2)
        return coopRate

    def getResults(self):
        """
        :return: tuple with a mean of cooperation rate and std of cooperation rate
        """
        return (self.coopResults, self.errorResults)

    def getLast1000PopForEveryRun(self) -> np.array:
        return np.array(self.ListLast1000EvolutionOfPopulationForEveryRun)
