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

    def calculateRange(self, seeds, maps):

        rangeSeeds= self.createRangeSeeds(seeds)
        self.logger.debug(rangeSeeds)

        cns=CalculateNextSeed()
        historySeeds=[]
        actualSeedsRange=rangeSeeds
        for map in maps:
            self.logger.debug(map["name"]+"-"+str(map["map"]))
            newSeedsRanges=[]
            for oneSeedRange in actualSeedsRange:
                self.logger.debug("seed range: \t"+str(oneSeedRange))
                seedRanges=cns.calcRange(map, oneSeedRange)
                newSeedsRanges+=seedRanges

            actualSeedsRange=newSeedsRanges
            historySeeds.append(newSeedsRanges)
            self.logger.debug("new seed ranges: "+str(newSeedsRanges))


        self.logger.debug("Last seeds array: "+str(historySeeds[len(historySeeds)-1]))
        return historySeeds[len(historySeeds)-1]

    def createRangeSeeds(self, seeds):
        rangeSeeds=[]
        for index in range(0,len(seeds),2):
            seedrange=[]
            seedrange.append(seeds[index])
            seedrange.append(seeds[index]+seeds[index+1]-1)
            rangeSeeds.append(seedrange)

        return rangeSeeds