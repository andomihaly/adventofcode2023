from loggercontext import LoggerContext
from calculatenextseed import CalculateNextSeed

class CalculateSeeds():
    logger = LoggerContext()

    def calculate(self, seeds, maps):
        cns=CalculateNextSeed()
        self.logger.debug(str(seeds))
        historySeeds=[]
        actualseeds=seeds
        for map in maps:
            self.logger.debug(map["name"]+"-"+str(map["map"]))
            newseeds=[]
            for seed in actualseeds:
                newseed=cns.calc(map, seed)
                self.logger.debug(str(seed)+"-"+str(newseed))
                newseeds.append(newseed)
            actualseeds=newseeds
            historySeeds.append(newseeds)
            self.logger.debug(str(newseeds))
        self.logger.debug(str(historySeeds))
        return historySeeds[len(historySeeds)-1]