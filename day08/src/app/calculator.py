from loggercontext import LoggerContext

class Calculator():
    logger = LoggerContext()

    def calculate(self, route, network):
        self.logger.debug(network)
        self.logger.debug(route)
        i=0
        stepCounter=0
        actualPosition="AAA"
        while(i<10):
            for nextMove in route:
                stepCounter+=1
                if nextMove=="L":
                    actualPosition=network[actualPosition][0]
                else:
                    actualPosition=network[actualPosition][1]
                if actualPosition=="ZZZ":
                    break
            if actualPosition=="ZZZ":
                break
            i+=1
        if(actualPosition!="ZZZ"):
            raise Exception("Destiniation is not find whitin 10 loops")


        return stepCounter
