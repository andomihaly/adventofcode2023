from loggercontext import LoggerContext
from math import lcm
from functools import reduce


class Calculator():
    logger = LoggerContext()

    def calculate(self, route, network):
        self.initRouteCalculator(network, route)
        startPosition = "AAA"
        self.findARoute(startPosition,"ZZZ")

        return self.firstStop[startPosition]

    def calculateGhost(self, route, network):
        self.initRouteCalculator(network, route)
        ghosts = self.collectStartingPoint()
        for startPosition in ghosts:
            self.findARoute(startPosition,"Z")

        return self.calculateLCM(self.firstStop)

    def initRouteCalculator(self, network, route):
        self.logger.debug(network)
        self.logger.debug(route)
        self.network = network
        self.route = route
        self.firstStop = {}

    def findARoute(self, startPosition, stopper):
        stepCounter = 0
        emergencyBreak = 0
        emergencyBreakMax = 99

        position = startPosition
        while (emergencyBreak < emergencyBreakMax):
            position, stepCounter = self.goARoute(position, stepCounter, stopper)
            if position.endswith(stopper):
                break
            emergencyBreak += 1

        self.raiseAnExceptionIfRouteNotFound(emergencyBreak, emergencyBreakMax, startPosition)

        self.firstStop[startPosition] = stepCounter

    def goARoute(self, position, stepCounter, stopper):
        for nextTurn in self.route:
            position = self.doAStep(nextTurn, position)
            stepCounter += 1
            if position.endswith(stopper):
                break
        return position, stepCounter

    def doAStep(self, nextTurn, position):
        if nextTurn == "L":
            position = self.network[position][0]
        else:
            position = self.network[position][1]
        return position

    def raiseAnExceptionIfRouteNotFound(self, emergencyBreak, emergencyBreakMax, startPosition):
        if emergencyBreak == emergencyBreakMax:
            raise Exception(
                "Destination is not find from " + startPosition + " with in " + str(emergencyBreakMax) + " loops")

    def calculateLCM(self, firstStop):
        sum = 1
        for item in firstStop:
            sum = lcm(sum, firstStop[item])
        return sum

    def collectStartingPoint(self):
        startPos = []
        for position in self.network:
            if (position[2] == "A"):
                startPos.append(position)
        self.logger.debug(str(startPos))
        return startPos

    def isFinish(self, positions):
        for pos in positions:
            if (not pos[2] == "Z"):
                return False
        return True
