from camelcard import CamelCard


class Parser():
    def parse(self, input):
        cards = []
        # QQQJA 483
        for row in input:
            card, bid = row.split(" ")
            cards.append(CamelCard(card, bid))
        return cards
