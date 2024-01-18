from Card import Card

class CardCompare:
    SAME = 0
    FIRST = 1
    SECOND = 2

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
    def compareNames(cardName1, cardName2):
        if cardName1 == cardName2:
            return CardCompare.SAME
        return CardCompare.FIRST if cardName1 < cardName2 else CardCompare.SECOND
    
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
        
        # Filter out basics, then nonbasic lands.
        # Sort by color, then CMC, then name alphabetically

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
        
    
