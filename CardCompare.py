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

    def compare(card1: Card, card2: Card):
        if card1.name == card2.name:
            return CardCompare.SAME
        # Sort by color, then CMC, then name alphabetically
        colorCompare = CardCompare.compareColors(card1.colors, card2.colors)
        if colorCompare != CardCompare.SAME:
            return colorCompare
        cmcCompare = CardCompare.compareCMC(card1.cmc, card2.cmc)
        if cmcCompare != CardCompare.SAME:
            return cmcCompare
        nameCompare = CardCompare.compareNames(card1.name, card2.name)
        return nameCompare
        
    
