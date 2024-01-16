import scrython

class Card:

    def __init__(self):
        self.name = None
        self.colors = None


    def __init__(self, name):
        card = scrython.cards.Named(fuzzy=name)
        self.initFromScryfall(card)

    def initFromScryfall(self, scryfallCard):
        self.name = scryfallCard.name().replace("//", "--")
        self.cmc = scryfallCard.cmc()
        if scryfallCard.layout() != 'normal':
            raise Exception("Not normal")
        self.colors = scryfallCard.colors()
