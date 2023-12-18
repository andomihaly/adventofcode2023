import re
from loggercontext import LoggerContext

class FindNumberInText():
    textToNumber=dict()
    textToNumber["zero"]=0
    textToNumber["one"]=1
    textToNumber["two"]=2
    textToNumber["three"]=3
    textToNumber["four"]=4
    textToNumber["five"]=5
    textToNumber["six"]=6
    textToNumber["seven"]=7
    textToNumber["eight"]=8
    textToNumber["nine"]=9
    reverseTextToNumber=dict()
    reverseTextToNumber["orez"]=0
    reverseTextToNumber["eno"]=1
    reverseTextToNumber["owt"]=2
    reverseTextToNumber["eerht"]=3
    reverseTextToNumber["ruof"]=4
    reverseTextToNumber["evif"]=5
    reverseTextToNumber["xis"]=6
    reverseTextToNumber["neves"]=7
    reverseTextToNumber["thgie"]=8
    reverseTextToNumber["enin"]=9
    logger = LoggerContext()

    def findNumber(self, text):
        number = self.convertTextNumberToDigit(text)
        self.logger.info("text: "+text+self.addTab(text)+" number: \t"+str(number))
        return number

    def convertTextNumberToDigit(self, text):
        oldtext = text
        self.logger.debug("original:\t\t"+oldtext)
        firstNumber = self.getFirstNumberInText(text)
        text = self.replaceNumberTextFrom(text)
        lastNumber = self.getLastNumberInText(text)
        self.logger.debug("first letter:\t"+str(firstNumber)+"\tlastletter:\t"+str(lastNumber))
        return int(str(firstNumber)+str(lastNumber))

    def getFirstNumberInText(self, text):
        numbers = re.findall(r'\d|zero|one|two|three|four|five|six|seven|eight|nine',text)
        firstNumber = -1
        for nextNumber in numbers:
            if (nextNumber.isnumeric()):
                firstNumber = int(nextNumber)
            else:
                firstNumber = self.textToNumber[nextNumber]
            break
        return firstNumber

    def replaceNumberTextFrom(self, text):
        newText=text
        numbers = re.findall(r'\d|zero|one|two|three|four|five|six|seven|eight|nine',text)
        for nextNumber in numbers:
            if (not nextNumber.isnumeric()):
                self.logger.debug("cserelendo: "+nextNumber)
                newText=text.replace(nextNumber, str(self.textToNumber[nextNumber]), 1)
            break
        return newText

    def getLastNumberInText(self, text):
        reverseText = text[::-1]
        numbers = re.findall(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin',reverseText)
        lastNumber=-1
        for nextNumber in numbers:
            if (nextNumber.isnumeric()):
                lastNumber = int(nextNumber)
            else:
                lastNumber = self.reverseTextToNumber[nextNumber]
            break
        return lastNumber
    
    def addTab(self, text):
        if (len(text)>10):
            return "\t"
        else:
            return "\t\t"