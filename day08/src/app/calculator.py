from loggercontext import LoggerContext
from math import lcm
from functools import reduce

class Calculator():
    logger = LoggerContext()

    def calculate(self, route, network):
        self.logger.debug(network)
        self.logger.debug(route)
        emergencyBreak = 0
        stepCounter = 0
        actualPosition = "AAA"
        while (emergencyBreak < 50):
            for nextMove in route:
                stepCounter += 1
                if nextMove == "L":
                    actualPosition = network[actualPosition][0]
                else:
                    actualPosition = network[actualPosition][1]
                if actualPosition == "ZZZ":
                    break
            if actualPosition == "ZZZ":
                break
            emergencyBreak += 1
        if (actualPosition != "ZZZ"):
            raise Exception("Destiniation is not find whitin 10 loops")

        return stepCounter

    def calculateGhost(self, route, network):
        self.logger.debug(network)
        self.logger.debug(route)

        firstStop={}
        ghosts=self.collectStartingPoint(network)
        for position in ghosts:
            startPos=position
            stepCounter = 0
            emergencyBreak = 0
            while (emergencyBreak < 100):
                for nextTurn in route:
                    stepCounter += 1
                    if nextTurn == "L":
                        position=network[position][0]
                    else:
                        position=network[position][1]
                    if position.endswith('Z'):
                        break
                if position.endswith('Z'):
                    break
                emergencyBreak += 1
            if not position.endswith('Z'):
                raise Exception("Destination is not find with in 100 loops")
            firstStop[startPos]=stepCounter

        return self.calculateLCM(firstStop)

    def calculateLCM(self, firstStop):
        sum = 1
        for item in firstStop:
            sum = lcm(sum, firstStop[item])
        return sum

    def collectStartingPoint(self, network):
        startPos = []
        for position in network:
            if (position[2] == "A"):
                startPos.append(position)
        self.logger.debug(str(startPos))
        return startPos

    def isFinish(self, positions):
        for pos in positions:
            if (not pos[2] == "Z"):
                return False
        return True
