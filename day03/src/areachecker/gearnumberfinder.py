from loggercontext import LoggerContext

class GearNumberFinder():
    logger=LoggerContext()
    def findGearNumber(self, aboveRow, row, belowRow):
        self.aboveRow=aboveRow
        self.row = row
        self.belowRow=belowRow

        gearNumbers=[]
        for i in range(0,len(row)):
            if (row[i]=="*"):
                #candidate
                self.logger.debug(row + " index: "+str(i))
                numbers=self.findNumbers(i)
                self.logger.debug(str(numbers))
                if (len(numbers)>1):
                    gearNumbers.append(numbers)

        self.logger.debug("gear numbers in row: "+ str(gearNumbers))
        return gearNumbers

    def findNumbers(self, starIndex):
        beforeStar=self.findStartNumberIndexBeforeStar(starIndex)
        beforeBelowStar=self.findStartNumberIndexBeforeAndBelowStar(starIndex)
        beforeAboveStar=self.findStartNumberIndexBeforeAndAboveStar(starIndex)
        afterStar=self.findEndNumberIndexAfterStar(starIndex)
        afterBelowStar=self.findStartNumberIndexAfterAndBelowStar(starIndex)
        afterAboveStar=self.findStartNumberIndexAfterAndAboveStar(starIndex)
        self.logger.debug(str(starIndex)
                          + "\t" + str(beforeStar)
                          + "\t" + str(beforeBelowStar)
                          + "\t" + str(beforeAboveStar)
                          + "\t" + str(afterStar)
                          + "\t" + str(afterBelowStar)
                          + "\t" + str(afterAboveStar)
                          )
        numbers=[]
        #simple case
        if (not beforeStar==starIndex):
            numbers.append(int(self.row[beforeStar:starIndex]))
        if (not afterStar==starIndex):
            numbers.append(int(self.row[starIndex+1:afterStar+1]))
        numbers += self.parseNumberFromText(self.aboveRow, starIndex, beforeAboveStar, afterAboveStar)
        numbers += self.parseNumberFromText(self.belowRow, starIndex, beforeBelowStar, afterBelowStar)
        return numbers

    def parseNumberFromText(self, actualRow, starIndex, startIndex, endIndex):
        #normal row 8 case: 12.45, 12..., ...45, 12345, 123.., ..345, ....., ..3..
        numbers=[]
        if (actualRow[starIndex].isnumeric()):
            #case 4,5,6
            if(not startIndex==starIndex and not endIndex==starIndex):
                numbers.append(int(actualRow[startIndex:endIndex+1]))
            else:
                if(not startIndex==starIndex):
                    numbers.append(int(actualRow[startIndex:starIndex+1]))
                else:
                    if(not endIndex==starIndex):
                        numbers.append(int(actualRow[starIndex:endIndex+1]))
                    else:
                        numbers.append(int(actualRow[starIndex:starIndex+1]))

        else:
            #case 1,2,3
            if (not startIndex==starIndex):
                numbers.append(int(actualRow[startIndex:starIndex]))
            if (not endIndex==starIndex):
                numbers.append(int(actualRow[starIndex+1:endIndex+1]))
        return numbers

    def findEndNumberIndexAfterStar(self, starIndex):
        return self.findStartNumberIndexAfter(starIndex, self.row)

    def findStartNumberIndexBeforeStar(self, starIndex):
        return self.findStartNumberIndexBefore(starIndex, self.row)

    def findStartNumberIndexAfterAndAboveStar(self, starIndex):
        return self.findStartNumberIndexAfter(starIndex, self.aboveRow)

    def findStartNumberIndexBeforeAndAboveStar(self, starIndex):
        return self.findStartNumberIndexBefore(starIndex, self.aboveRow)

    def findStartNumberIndexAfterAndBelowStar(self, starIndex):
        return self.findStartNumberIndexAfter(starIndex, self.belowRow)

    def findStartNumberIndexBeforeAndBelowStar(self, starIndex):
        return self.findStartNumberIndexBefore(starIndex, self.belowRow)

    def findStartNumberIndexBefore(self, starIndex, actualRow):
        index=starIndex
        while (index>0 and actualRow[index-1].isnumeric()):
            index-=1
        return index

    def findStartNumberIndexAfter(self, starIndex, actualRow):
        self.logger.debug("row: "+ actualRow + "star index: "+str(starIndex))
        index=starIndex
        while (index<len(actualRow)-1 and actualRow[index+1].isnumeric()):
            index+=1
        self.logger.debug("afterIndex: "+ str(index))
        return index