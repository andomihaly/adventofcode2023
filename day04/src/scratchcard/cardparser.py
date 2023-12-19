import re
from card import Card

class CardParser():
    def pars(self, text):
        card = Card()
        subTexts=text.split(": ")
        baseData=subTexts[0].split(" ")
        card.name=baseData[0]
        card.id=int(baseData[1])
        numbersText=subTexts[1].split(" | ")
        numbers = re.findall(r'\d+', numbersText[0])
        card.numbers = [int(num) for num in numbers ]
        winningNumbers = re.findall(r'\d+', numbersText[1])
        card.winningNumbers = [int(num) for num in winningNumbers]

        return card
