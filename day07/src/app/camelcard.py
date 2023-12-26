from enum import Enum


class CamelCardRank(Enum):
    FiveOfAKind = 1
    FourOfAKind = 2
    FullHouse = 3
    ThreeOfAKind = 4
    TwoPair = 5
    OnePair = 6
    HighCard = 7


class CamelCard:
    def __init__(self, cards, bet):
        self.cards = tuple(cards)
        self.bet = int(bet)
        self.generateMap()
        self.calculateRank()

    def calculateRank(self):
        self.rank = CamelCardRank.HighCard
        if (self.numberOfSameCards[0] == 5):
            self.rank = CamelCardRank.FiveOfAKind
        elif (self.numberOfSameCards[0] == 4):
            self.rank = CamelCardRank.FourOfAKind
        elif (self.numberOfSameCards[0] == 3 and self.numberOfSameCards[1] == 2):
            self.rank = CamelCardRank.FullHouse
        elif (self.numberOfSameCards[0] == 3 and self.numberOfSameCards[1] == 1):
            self.rank = CamelCardRank.ThreeOfAKind
        elif (self.numberOfSameCards[0] == 2 and self.numberOfSameCards[1] == 2):
            self.rank = CamelCardRank.TwoPair
        elif (self.numberOfSameCards[0] == 2 and self.numberOfSameCards[1] == 1):
            self.rank = CamelCardRank.OnePair

    def generateMap(self):
        map = {}
        for letter in self.cards:
            map[letter] = 0
        for letter in self.cards:
            map[letter] += 1
        self.numberOfSameCards = []
        for item in map:
            self.numberOfSameCards.append(map[item])
        self.numberOfSameCards = sorted(self.numberOfSameCards, reverse=True)
