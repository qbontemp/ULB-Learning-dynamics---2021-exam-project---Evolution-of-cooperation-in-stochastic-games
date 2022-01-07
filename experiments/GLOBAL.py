"""
Main experiment simulation functions
"""

from os.path import exists
from MonteCarlo import MonteCarlo
from prisoner_dilemma.DSD import DSD
from prisoner_dilemma.DSI import DSI
from prisoner_dilemma.OnlyOneGame import OnlyOneGame
from prisoner_dilemma.PDSD import PDSD
from prisoner_dilemma.PSD import PSD
from prisoner_dilemma.PSI import PSI
import numpy
from Strategy import GeneratorMemoryOne
from typing import List
from Strategy import Action

PATH_TO_DATA_FOLDER = "dataSaver"

#Game properties
NB_ROUNDS = 100  # number of rounds used to calculate static payoffs and cooperation rates

# Monte Carlo properties
NB_STEP = 100000  # number of time steps
NB_INIT = 0
NB_RUN = 100  # number of simulations to average



def generateDataStaticMatrix(gameName : str,error : float,b1 :float,b2:float,c:float,probabilityMoveStayState2:float or None) -> (List[List[float]],(List[List[float]])):
    """
    If it doesn't exist already, generate the data for each strategy, their payoffs and their cooperation rates with others strategies and save them

    :param gameName: game type
    :param error: error rate
    :param b1: b1
    :param b2: b2
    :param c: c
    :param probabilityMoveStayState2: transition probability p
    :return: Tuple(payoff matrix, coop rate matrix)
    """


    gameParameterUsedForGeneration = "{}_b1_{}_b2_{}_c_{}_error_{}_probabilityMoveStayState2_{}".format(gameName,b1,b2,c,error,probabilityMoveStayState2)
    nameCoopRateFile = "{}/COOP_RATE_{}.npy".format(PATH_TO_DATA_FOLDER,gameParameterUsedForGeneration)
    namePayoffFile = "{}/PAYOFF_{}.npy".format(PATH_TO_DATA_FOLDER,gameParameterUsedForGeneration)
    print(gameParameterUsedForGeneration)

    if(exists(nameCoopRateFile) and exists(namePayoffFile)):
        print("Data for {} is found, loading data".format(gameParameterUsedForGeneration))
        coopRate = numpy.load(nameCoopRateFile)
        payoff = numpy.load(namePayoffFile)

    elif(exists(nameCoopRateFile) or exists(namePayoffFile)):
        raise Exception("Fatal error, call the team !")

    else:
        startingPreceding = [[Action.COOP, Action.COOP], [Action.COOP, Action.DEFECT], [Action.DEFECT, Action.COOP],
                             [Action.DEFECT, Action.DEFECT]]

        strategies = GeneratorMemoryOne(error=error).getStrategies()

        print("Beginning calculation of static values {}".format(gameParameterUsedForGeneration))

        game = None
        if (probabilityMoveStayState2 != None):
            if (gameName == "PDSD"): #Probaliblity Deterministic State-dependent #This name was invented
                game = PDSD(startingPreceding, strategies, NB_ROUNDS, b1, b2, c,
                                  probabilityMoveStayState2)

            elif (gameName == "PSD"):  #Probabilistic State-dependent
                game = PSD(startingPreceding, strategies, NB_ROUNDS, b1, b2, c,
                                 probabilityMoveStayState2)

            elif (gameName == "PSI"): #Probabilistic State-independent
                game = PSI(startingPreceding, strategies, NB_ROUNDS, b1, b2, c,
                                 probabilityMoveStayState2)

        else:
            if (gameName == "DSD"): # Deterministic State-dependent
                game = DSD(startingPreceding, strategies, NB_ROUNDS, b1, b2, c)

            elif (gameName == "DSI"): #Deterministic State-independent
                game = DSI(startingPreceding, strategies,NB_ROUNDS, b1, b2, c)

            elif(gameName == "OG1"): # Only game 1
                game = OnlyOneGame(startingPreceding, strategies,NB_ROUNDS, b1, c)

            elif (gameName == "OG2"): # Only game 2
                game = OnlyOneGame(startingPreceding, strategies, NB_ROUNDS, b2, c)

        if (game == None):
            print("Error creating game")
            exit()

        payoff,coopRate = game.getPayoffs(),game.getCooperationRate()

        numpy.save(namePayoffFile, payoff)
        numpy.save(nameCoopRateFile, coopRate)

    return (payoff,coopRate)


def generateDataMonteCarlo(payoffOfStrategies : numpy.array,coopOfStrategies : numpy.array,initialPopulation : int,Z : int ,beta : float ,mu : float, gameParameterUsedForGeneration : str):
    """
    Generates the data for Monte Carlo if doesn't exist

    :param payoffOfStrategies: payoff matrix
    :param coopOfStrategies: coop rate matrix
    :param initialPopulation: initial strategy, -1 for a random population
    :param Z: population size
    :param beta: selection strength
    :param mu: mutation rate
    :param gameParameterUsedForGeneration: string containing relevant game parameters
    """
    monteCarloParameter = "initialPopulation_{}_Z_{}_beta_{}_mu_{}_{}".format(initialPopulation,Z,beta,mu,gameParameterUsedForGeneration)
    nameMeanCoop = "{}/MC_MEAN_COOP_{}.npy".format(PATH_TO_DATA_FOLDER,monteCarloParameter)
    nameSTDCoop = "{}/MC_STD_COOP_{}.npy".format(PATH_TO_DATA_FOLDER,monteCarloParameter)
    namePop = "{}/MC_POP_{}.npy".format(PATH_TO_DATA_FOLDER,monteCarloParameter)
    if(exists(nameMeanCoop) and exists(nameSTDCoop) and exists(namePop)):
        print("Data for {} is found, no simulation".format(monteCarloParameter))

    elif(exists(nameMeanCoop) or exists(nameSTDCoop) or exists(namePop)):
        raise Exception("Fatal error, call the team !")

    else:
        print("Beginning Monte Carlo simulation of {}".format(monteCarloParameter))
        simulation = MonteCarlo(Z, beta, mu, payoffOfStrategies,coopOfStrategies, initialPopulation)

        simulation.simulate(NB_STEP, NB_INIT, NB_RUN)

        meanCoop, stdCoop = simulation.getResults()
        popList = simulation.getLast1000PopForEveryRun()

        numpy.save(nameMeanCoop, meanCoop)
        numpy.save(nameSTDCoop, stdCoop)
        numpy.save(namePop, popList)


def generateData(initialPopulation : int,Z : int, beta : float,mu : float,gameName : str,error : float,b1 : float ,b2 :float ,c : float ,probabilityMoveStayState2 :float or None ):
    """
    Generates the data of the static matrices and the Monte Carlo simulation
    :param initialPopulation:  initial strategy, -1 for random
    :param Z: population size
    :param beta: selection strength
    :param mu: mutation rate
    :param gameName: game type
    :param error: error rate
    :param b1: b1
    :param b2: b2
    :param c: c
    :param probabilityMoveStayState2: transition probability (for probabilistic games only)
    """
    gameParameterUsedForGeneration = "{}_b1_{}_b2_{}_c_{}_error_{}_probabilityMoveStayState2_{}".format(gameName,b1,b2,c,error,probabilityMoveStayState2)
    payoff, coopRate = generateDataStaticMatrix(gameName,error,b1,b2,c,probabilityMoveStayState2)
    generateDataMonteCarlo(payoff,coopRate,initialPopulation,Z,beta,mu,gameParameterUsedForGeneration)

