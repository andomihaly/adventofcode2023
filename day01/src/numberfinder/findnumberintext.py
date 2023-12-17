import re
from loggercontext import LoggerContext

class FindNumberInText():
    mixedTextNumber = ["eighthreeight","zerone","threeight","sevenine","nineight","eightwo","twone","eighthree","fiveight"]
    mixedDigitNumber = ["8hre8","0ne","3ight","7ine","9ight","8wo","2ne","8hree","5ight"]
    textNumber = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digitNumber = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    logger = LoggerContext()
    def findNumber(self, text):
        textWithDigit = self.convertTextNumberToDigit(text)
        number = self.getNumberFromDigits(textWithDigit)
        #self.saveIfSpecialCases(text, textWithDigit, number)
        #self.saveIfTextCount(text, textWithDigit, number)
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

    def saveIfSpecialCases(self,text, digittext, number):
        res = any(ele in text for ele in self.textNumber)
        if res:
            file1 = open("specialcases2.txt", "a")
            file1.write(text+"\t "+digittext+"\t "+str(number)+"\n")
            file1.close()
    def saveIfTextCount(self,text, digittext, number):
        number2 = self.getNumberFromDigits(text)
        if number!=number2:
            file1 = open("specialcasestextcount3.txt", "a")
            file1.write(text+"\t "+digittext+"\t "+str(number)+"\n")
            file1.close()
        else:
            file1 = open("normalcase4.txt", "a")
            file1.write(text+"\t "+digittext+"\t "+str(number)+"\n")
            file1.close()

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