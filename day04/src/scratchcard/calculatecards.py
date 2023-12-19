from cardparser import CardParser
class CalculateCards():
    def sumWinningScore(self, cards):
        sum=0
        cardParser = CardParser()
        for cardText in cards:
            sum+=cardParser.pars(cardText).score()

        return sum

