from camelcard import CamelCard
from camelcard import CamelCardWithJoker


class Parser():
    def parse(self, input):
        cards = []
        # QQQJA 483
        for row in input:
            card, bid = row.split(" ")
            cards.append(CamelCard(card, bid))
        return cards

    def parseWithJoker(self, input):
        cards = []
        # QQQJA 483
        for row in input:
            card, bid = row.split(" ")
            cards.append(CamelCardWithJoker(card, bid))
        return cards
