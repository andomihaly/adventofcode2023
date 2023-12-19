from cardparser import CardParser
class CalculateCardCopies():
    def sumCopies(self, cards):
        cardParser = CardParser()
        copies=self.initCopies(len(cards))
        print(copies)
        for i in range(0,len(cards)):
            numberOfHit=cardParser.pars(cards[i]).getNumberOfHit()
            for i1 in range(0,numberOfHit):
                copies[i+1+i1]+=(1*copies[i])
        return sum(copies)

    def initCopies(self, numberOfCards):
        copies=[]
        for i in range(0,numberOfCards):
            copies.append(1)
        return copies
