import re
from loggercontext import LoggerContext

class FindNumberInText():
    mixedTextNumber = ["nineight","eightwo","twone","eighthree"]
    mixedDigitNumber = ["9ight","8wo","2ne","8hree"]
    textNumber = ["zero",  "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digitNumber = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    logger = LoggerContext()
    def findNumber(self, text):
        textWithDigit = self.convertTextNumberToDigit(text)
        number = self.getNumberFromDigits(textWithDigit)
        self.logger.info("text: "+text+self.addTab(text)+" just digit: "+textWithDigit+self.addTab(textWithDigit)+" number: \t"+str(number))
        return number

    def convertTextNumberToDigit(self, text):
        oldtext = text
        self.logger.debug("original:\t\t"+oldtext)
        for i1 in range(len(self.mixedTextNumber)):
            text = text.replace(self.mixedTextNumber[i1], self.mixedDigitNumber[i1])
            self.logger.debug("i1 case:\t"+text+"-- "+self.mixedTextNumber[i1]+"-"+ self.mixedDigitNumber[i1] )
        self.logger.debug("after special case:\t"+text)
        for i in range(len(self.textNumber)):
            text = text.replace(self.textNumber[i], self.digitNumber[i])
        self.logger.debug("new text:\t\t" + text)
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