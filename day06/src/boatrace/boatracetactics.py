class BoatRaceTactics():

    def findWinningOptionsInRaces(self,races):
        options=[]
        for race in races:
            options.append(self.findWinningOptions(race))
        return options

    def findWinningOptions(self, race):
        time=race[0]
        distance=race[1]
        winningOption=[]
        for i in range(1,time):
            way=(time-i)*i
            if (way>distance):
                winningOption.append(i)
        return winningOption