from loggercontext import LoggerContext


class Calculator():
    logger = LoggerContext()

    def calculate(self, route, network):
        self.logger.debug(network)
        self.logger.debug(route)
        i = 0
        stepCounter = 0
        actualPosition = "AAA"
        while (i < 50):
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
            i += 1
        if (actualPosition != "ZZZ"):
            raise Exception("Destiniation is not find whitin 10 loops")

        return stepCounter

    def calculateGhost(self, route, network):
        self.logger.debug(network)
        self.logger.debug(route)
        i = 0
        stepCounter = 0
        actualPositions = self.collectStartingPoint(network)
        while (i < 500000000000):
            for nextMove in route:
                stepCounter += 1
                nextPositions = []
                for position in actualPositions:
                    if nextMove == "L":
                        nextPositions.append(network[position][0])
                    else:
                        nextPositions.append(network[position][1])
                actualPositions = nextPositions
                self.logger.debug(str(stepCounter) + ". step:")
                self.logger.debug(str(actualPositions))
                if self.isFinish(actualPositions):
                    break
            if self.isFinish(actualPositions):
                break
            i += 1
        if not self.isFinish(actualPositions):
            raise Exception("Destination is not find with in X loops")

        return stepCounter

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
