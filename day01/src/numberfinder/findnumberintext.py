import re
from loggercontext import LoggerContext

class FindNumberInText():
    textNumber = ["zero", "two", "one", "nine", "five", "three", "eight", "four", "six", "seven"]
    digitNumber = ["0", "2", "1", "9", "5", "3", "8", "4", "6", "7"]
    logger = LoggerContext()
    def findNumber(self, text):
        textWithDigit = self.convertTextNumberToDigit(text)
        number = self.getNumberFromDigits(textWithDigit)
        self.logger.info("text: "+text+self.addTab(text)+" just digit: "+textWithDigit+self.addTab(textWithDigit)+" number: \t"+str(number))
        return number

    def convertTextNumberToDigit(self, text):
        oldtext = text
        self.logger.debug("old:\t"+oldtext)
        for i in range(len(self.textNumber) - 1):
            text = text.replace(self.textNumber[i], self.digitNumber[i])
        self.logger.debug(" new text: \t" + text)
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

    def addTab(self, text):
        if (len(text)>10):
            return "\t"
        else:
            return "\t\t"