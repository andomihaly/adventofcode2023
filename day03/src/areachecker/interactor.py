from loggercontext import LoggerContext
from findnumberwithborder import FindNumberWithBorder
from gearnumberfinder import GearNumberFinder

class Interactor():
    logger = LoggerContext()

    def __init__(self, contentLoader):
        self.contentLoader = contentLoader

    def run(self):
        print(self.logger)
        self.logger.info("process started")
        fileContent = self.contentLoader.loadContent()
        self.logger.info("content loaded")
        #business logic
        result = self.calculateSumOfNumber(fileContent)

        self.logger.info("sum is calculated:"+str(result))

    def calculateSumOfNumber(self, fileContent):
        rows = self.extendContent(fileContent)
        findNumber = FindNumberWithBorder()
        sum=0
        for index in range(1,len(rows)-1):
            numbers=findNumber.findBorderedNumbers(rows[index-1],rows[index],rows[index+1])
            self.logger.warning("row no:\t"+str(index)+" \tfindNumbers: \t"+str(numbers))
            for number in numbers:
                sum+=number
        return sum

    def extendContent(self, fileContent):
        rows=fileContent.splitlines()
        numberOfCharacterInRow = len(rows[0])
        temprow=""
        for i in range(numberOfCharacterInRow):
            temprow+="."
        extendedRows=[]
        extendedRows.append(temprow)
        extendedRows +=rows
        extendedRows.append(temprow)
        self.logger.warning(extendedRows)
        return extendedRows

    def runGearNumberSum(self):
        print(self.logger)
        self.logger.info("process started")
        fileContent = self.contentLoader.loadContent()
        self.logger.info("content loaded")
        #business logic
        result = self.calculateGearNumberSum(fileContent)

        self.logger.info("sum is calculated:"+str(result))

    def calculateGearNumberSum(self, fileContent):
        rows = self.extendContent(fileContent)
        gearNumberFinder = GearNumberFinder()
        sum=0
        for index in range(1,len(rows)-1):
            numbers=gearNumberFinder.findGearNumber(rows[index-1],rows[index],rows[index+1])
            self.logger.warning("row no:\t"+str(index)+" \tfindNumbers: \t"+str(numbers))
            for number in numbers:

                sum+=number[0]*number[1]
        return sum