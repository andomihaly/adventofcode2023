import re
from loggercontext import LoggerContext

class Interactor():
    textNumber = ["zero", "two", "one", "nine", "five", "three", "eight", "four", "six", "seven"]
    digitNumber = ["0", "2", "1", "9", "5", "3", "8", "4", "6", "7"]
    logger = LoggerContext()

    def __init__(self, contentLoader):
        self.contentLoader = contentLoader

    def run(self):
        print(self.logger)
        self.logger.info("process started")
        fileContent = self.contentLoader.loadContent()
        self.logger.info("content loaded")
        total = self.calculateAndSum(fileContent)
        self.logger.info("sum is calculated:"+str(total))
        print(total)

    def calculateAndSum(self, rows):
        rows = rows.splitlines()
        total = 0
        for row in rows:
            total += self.findNumber(row)
        return total

    def findNumber(self, text):
        text = self.convertTextNumberToDigit(text)
        return self.getNumberFromDigits(text)

    def convertTextNumberToDigit(self, text):
        self.logger.debug("original: " + text)
        for i in range(len(self.textNumber) - 1):
            text = text.replace(self.textNumber[i], self.digitNumber[i])
        self.logger.debug("new:      " + text)
        return text

    def getNumberFromDigits(self, text):
        digits = re.findall(r'\d', text)
        s1 = self.getFirstDigit(digits)
        s2 = self.getLastDigit(digits)
        number = s1 + s2
        self.logger.debug(number)
        return int(number)

    def getFirstDigit(self, digits):
        return digits[0]

    def getLastDigit(self, digits):
        return digits[len(digits) - 1]
