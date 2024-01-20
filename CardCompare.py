from Card import Card

class CardCompare:
    SAME = 0
    FIRST = 1
    SECOND = 2

    _population = []
    _populationNames = []

    def register(self, name, sortAfter = True):
        if name in self._populationNames:
            if sortAfter:
                self.sortPopulation()
            return name
        else: 
            newCard = Card(name)
            if not newCard.name in self._populationNames:
                self.registerAndSort(newCard)
                #self.registerAndSort(newCard, sort = sortAfter)
        return newCard.name

    def getValue(self, name):
        n = self.register(name)
        return self._populationNames.index(n)

    def clear(self):
        self._population.clear()
        self._populationNames.clear()

    def bulkRegister(self, newNamesList):
        for name in newNamesList:
            self.register(name, sortAfter = name == newNamesList[-1])

    def registerAndSort(self, newCard, sort = True):
        newPop = [newCard]
        newPop.extend(self._population)
        self._population = newPop
        if sort:
            self.sortPopulation()
        self.regenNames()

    def regenNames(self):
        self._populationNames.clear()
        for c in self._population:
            self._populationNames.append(c.name)

    def sortPopulation(self):
        if len(self._population) > 1:
            repeatIsNecessary = True
            iterations = 0
            while repeatIsNecessary:
                repeatIsNecessary = False
                for i in range(len(self._population) - 1):
                    result = CardCompare.compare( self._population[i], self._population[i+1] )
                    if result == CardCompare.SECOND:
                        repeatIsNecessary = True
                        self.swapCards(i, i+1)
                iterations += 1

    def swapCards(self, index1:int, index2: int):
        tempCard = self._population[index1]
        self._population[index1] = self._population[index2]
        self._population[index2] = tempCard

    def compareNormals(c1: Card, c2: Card):
        c1Normal = c1.layout == 'normal'
        c2Normal = c2.layout == 'normal'

        # Prioritize normals
        if c1Normal and c2Normal:
            return CardCompare.SAME
        if c1Normal:
            return CardCompare.FIRST        
        if c2Normal:
            return CardCompare.SECOND
        
        # If neither are "normal", group by layout then alphabetically.
        result = CardCompare.compareWords(c1.layout, c2.layout)
        if result != CardCompare.SAME:
            return result
        
        result = CardCompare.compareNames(c1.name, c2.name)
        return result

    def compareColors(cardColors1, cardColors2):
        if cardColors1 == cardColors2:
            return CardCompare.SAME
        def custom_sort(lst):
            return (len(lst)==0, len(lst), valuate(lst))

        def valuate(arr):
            val = 0
            for a in arr:
                val += 2 ** 'WUBRG'.index(a)
            return val

        testSort = [cardColors1, cardColors2]
        sorted_lists = sorted(testSort, key=custom_sort)

        return CardCompare.FIRST if cardColors1 == sorted_lists[0] else CardCompare.SECOND

    def compareWords(word1, word2):
        if word1 == word2:
            return CardCompare.SAME
        return CardCompare.FIRST if word1 < word2 else CardCompare.SECOND

    def compareNames(cardName1, cardName2):
        return CardCompare.compareWords(cardName1, cardName2)

    def compareCMC(cardCmc1, cardCmc2):
        if cardCmc1 == cardCmc2:
            return CardCompare.SAME
        return CardCompare.FIRST if cardCmc1 < cardCmc2 else CardCompare.SECOND

    def compareLand(c1Attribute, c1ColorId, c2Attribute, c2ColorId):
        if not (c1Attribute or c2Attribute):
            return CardCompare.SAME
        if c1Attribute and c2Attribute:
            return CardCompare.compareColors(c1ColorId, c2ColorId)
        if c1Attribute:
            return CardCompare.SECOND
        if c2Attribute:
            return CardCompare.FIRST
        raise Exception()

    def compareBasicLand(c1: Card, c2: Card):
        return CardCompare.compareLand(c1.isBasicLand, c1.color_identity, c2.isBasicLand, c2.color_identity)

    def compareNonBasicLand(c1: Card, c2: Card):
        return CardCompare.compareLand(c1.isLand, c1.color_identity, c2.isLand, c2.color_identity)

    def compare(card1: Card, card2: Card):
        if card1.name == card2.name:
            return CardCompare.SAME

        # Filter out non-normal layouts, basics, then nonbasic lands.
        # Sort by color, then CMC, then name alphabetically

        result = CardCompare.compareNormals(card1, card2)
        if result != CardCompare.SAME:
            return result

        result = CardCompare.compareBasicLand(card1, card2)
        if result != CardCompare.SAME:
            return result

        result = CardCompare.compareNonBasicLand(card1, card2)
        if result != CardCompare.SAME:
            return result

        result = CardCompare.compareColors(card1.colors, card2.colors)
        if result != CardCompare.SAME:
            return result

        result = CardCompare.compareCMC(card1.cmc, card2.cmc)
        if result != CardCompare.SAME:
            return result

        result = CardCompare.compareNames(card1.name, card2.name)
        return result

