import re
from loggercontext import LoggerContext

class FindNumberWithBorder():
    logger = LoggerContext()
    borderedNumbers=[]
    def findBorderedNumbers(self, aboveRow, row, belowRow):
        self.logger.debug("row: \t"+row)
        self.row = row
        self.aboveRow = aboveRow
        self.belowRow = belowRow
        self.borderedNumbers=[]
        self.chechRow()
        return self.borderedNumbers

    def chechRow(self):
        candidateNumbers = re.findall(r'\d+',self.row)
        for candidate in candidateNumbers:
            self.logger.debug("candiadate: \t"+candidate)
            self.isCandidateOk = False
            self.checkCandidte(candidate)
            if (self.isCandidateOk):
                self.borderedNumbers.append(int(candidate))
            #removetext
            lenght=len(candidate)
            position=self.row.find(candidate)
            self.row=self.row[0:position]+self.row[position+lenght:len(self.row)]
            self.aboveRow = self.aboveRow[lenght:len(self.aboveRow)]
            self.belowRow = self.belowRow[lenght:len(self.belowRow)]

    def checkCandidte(self, candidate):
        self.checkBelow(candidate)
        if (not self.isCandidateOk):
            self.checkAfter(candidate)
        if (not self.isCandidateOk):
            self.checkCorners(candidate)
        if (not self.isCandidateOk):
            self.checkSide(candidate)

    def checkBelow(self, candidate):
        index=self.row.find(candidate)
        if (index>0 and not self.row[index-1]=="."):
            self.isCandidateOk = True

    def checkAfter(self, candidate):
        index=self.row.find(candidate)+len(candidate)
        if (index<len(self.row) and not self.row[index]=="."):
            self.isCandidateOk = True

    def checkCorners(self, candidate):
        index=self.row.find(candidate)
        lastDigitIndex=index+len(candidate)
        if (index>0 and self.isGoodCharacter(self.aboveRow[index-1])):
            self.isCandidateOk = True
        if (lastDigitIndex<len(self.row) and self.isGoodCharacter(self.aboveRow[lastDigitIndex])):
            self.isCandidateOk = True
        if (index>0 and self.isGoodCharacter(self.belowRow[index-1])):
            self.isCandidateOk = True
        if (lastDigitIndex<len(self.row) and self.isGoodCharacter(self.belowRow[lastDigitIndex])):
            self.isCandidateOk = True

    def isGoodCharacter(self, char):
        if (char=="."):
            return False
        if (char.isnumeric()):
            return False
        return True

    def checkSide(self, candidate):
        index=self.row.find(candidate)
        lastDigitIndex=index+len(candidate)
        self.logger.debug("first index: \t"+str(index)+" last index:\t"+str(lastDigitIndex))
        subAboveRow = self.aboveRow[index:lastDigitIndex]
        self.checkSubSide(subAboveRow)
        subBelowRow = self.belowRow[index:lastDigitIndex]
        self.checkSubSide(subBelowRow)

    def checkSubSide(self, subText):
        self.logger.debug(subText)
        notDotText = re.findall(r'[^.0-9]',subText)
        self.logger.debug("find above row: "+ str(len(notDotText)))
        if (len(notDotText)>0):
            self.isCandidateOk = True