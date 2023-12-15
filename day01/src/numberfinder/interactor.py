import logging
import re


class Interactor():
    textNumber = ["zero", "two", "one", "nine", "five", "three", "eight", "four", "six", "seven"]
    digitNumber = ["0", "2", "1", "9", "5", "3", "8", "4", "6", "7"]

    def __init__(self, contentLoader):
        self.contentLoader = contentLoader

    def run(self):
        logging.basicConfig(level=logging.DEBUG)
        fileContent = self.contentLoader.loadContent()
        total = self.calculateAndSum(fileContent)
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
        logging.debug("original: " + text)
        for i in range(len(self.textNumber) - 1):
            text = text.replace(self.textNumber[i], self.digitNumber[i])
        logging.debug("new:      " + text)
        return text

    def getNumberFromDigits(self, text):
        digits = re.findall(r'\d', text)
        s1 = self.getFirstDigit(digits)
        s2 = self.getLastDigit(digits)
        number = s1 + s2
        logging.debug(number)
        return int(number)

    def getFirstDigit(self, digits):
        return digits[0]

    def getLastDigit(self, digits):
        return digits[len(digits) - 1]
