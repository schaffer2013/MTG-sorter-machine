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
        self.layout = scryfallCard.layout()
        self.url = scryfallCard.image_uris()['normal']
        if self.layout == 'normal':
            self.cmc = scryfallCard.cmc()
            self.colors = scryfallCard.colors()
            self.color_identity = scryfallCard.color_identity()
            self.type_line = scryfallCard.type_line()
            self.isBasicLand = "Basic" in self.type_line
            self.isLand = "Land" in self.type_line

        dummy = -1
