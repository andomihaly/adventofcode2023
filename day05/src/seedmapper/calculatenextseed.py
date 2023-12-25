class CalculateNextSeed():
    def calc(self, map, seed):
        for row in map["map"]:
            if (seed>=row[0] and seed<row[0]+row[2]):
                return seed+row[1]-row[0]
        return seed

    def calcRange(self, map, seedRange):

        self.lowerBound=seedRange[0]
        self.upperBound=seedRange[1]
        self.transformUpperBound=-1;
        self.transformLowerBound=1000000000000000000000
        self.newSeedRange = []
        for row in map["map"]:
            self.convertSeedsInMap(row)
        self.addSeedsWhichIsNotConverted()
        self.addIfFullOutOfRange(seedRange)

        self.checkNumberOfSeeds(seedRange,self.newSeedRange)

        return self.newSeedRange

    def checkNumberOfSeeds(self, seedIn, seedOut):
        print(seedIn)
        print(seedOut)
        sum1=seedIn[1]-seedIn[0]+1
        sum2=0;
        for seedRange in seedOut:
            sum2+=(seedRange[1]-seedRange[0]+1)
        if (not sum1==sum2):
           raise Exception("Extra seed added")

    def convertSeedsInMap(self, row):
        lowerBound = self.lowerBound
        upperBound = self.upperBound
        #cases: not in map, full part is in row, serveral row, half part is not in row
        self.inSideMapRow(lowerBound, row, upperBound)
        self.seedRangeUpperOut(lowerBound, row, upperBound)
        self.seedRangeLowerOut(lowerBound, row, upperBound)
        self.seedRangeLowerAndUpperOut(lowerBound, row, upperBound)

    def seedRangeLowerAndUpperOut(self, lowerBound, row, upperBound):
        if (self.isMapRowInSeedRangeOut(row[0], row[0] + row[2] - 1, lowerBound, upperBound)):
            self.newSeedRange.append([row[1], row[1] + row[2] - 1])
            if (row[2] + row[0] + 1 > self.transformUpperBound):
                self.transformUpperBound = row[2] + row[0]
            if (row[0] < self.transformLowerBound):
                self.transformLowerBound = row[0] - 1

    def seedRangeLowerOut(self, lowerBound, row, upperBound):
        if (self.isLowerBoundOut(row[0], row[0] + row[2] - 1, lowerBound, upperBound)):
            self.newSeedRange.append([row[1], upperBound + row[1] - row[0]])
            self.transformUpperBound = upperBound
            if (row[0] < self.transformLowerBound):
                self.transformLowerBound = row[0] - 1

    def seedRangeUpperOut(self, lowerBound, row, upperBound):
        if (self.isUpperBoundOut(row[0], row[0] + row[2] - 1, lowerBound, upperBound)):
            self.newSeedRange.append([lowerBound + row[1] - row[0], row[2] + row[1] - 1])
            if (row[2] + row[0] + 1 > self.transformUpperBound):
                self.transformUpperBound = row[2] + row[0]
            self.transformLowerBound = lowerBound

    def inSideMapRow(self, lowerBound, row, upperBound):
        if (self.isFullRange(row[0], row[0] + row[2] - 1, lowerBound, upperBound)):
            self.newSeedRange.append([lowerBound + row[1] - row[0], upperBound + row[1] - row[0]])
            self.transformUpperBound = upperBound
            self.transformLowerBound = lowerBound

    def addSeedsWhichIsNotConverted(self):
        if (self.transformLowerBound<1000000000000000000000 and self.transformLowerBound>self.lowerBound):
            self.newSeedRange.append([self.lowerBound,self.transformLowerBound])
        if (self.transformUpperBound>-1 and self.transformUpperBound<self.upperBound):
            self.newSeedRange.append([self.transformUpperBound,self.upperBound])

    def addIfFullOutOfRange(self, seedRange):
        if len(self.newSeedRange)==0:
            self.newSeedRange.append(seedRange)

    def isFullRange(self, mapLower, mapUpper, seedLower, seedUpper):
        lower=False
        upper=False
        if (mapLower<=seedLower and mapUpper>=seedLower):
            lower=True
        if (mapLower<=seedUpper and mapUpper>=seedUpper):
            upper=True
        return lower and upper

    def isUpperBoundOut(self, mapLower, mapUpper, seedLower, seedUpper):
        lower=False
        upper=False
        if (mapLower<=seedLower and mapUpper>=seedLower):
            lower=True
        if (mapLower<=seedUpper and mapUpper>=seedUpper):
            upper=True
        return lower and not upper

    def isLowerBoundOut(self, mapLower, mapUpper, seedLower, seedUpper):
        lower=False
        upper=False
        if (mapLower<=seedLower and mapUpper>=seedLower):
            lower=True
        if (mapLower<=seedUpper and mapUpper>=seedUpper):
            upper=True
        return not lower and upper

    def isMapRowInSeedRangeOut(self, mapLower, mapUpper, seedLower, seedUpper):
        if (seedLower<mapLower and seedUpper>mapUpper):
                return True
        return False