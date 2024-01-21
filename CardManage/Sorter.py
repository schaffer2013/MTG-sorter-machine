from CardManage.CardCompare import CardCompare

def minMax(arr):
  min = 100000000
  max = -min
  for a in arr:
    if a < min and a != Sorter.NO_CARD:
      min = a
    if a > max and a != Sorter.NO_CARD:
      max = a
  return (min, max)

def minMaxIndex(arr):
  (minimum, maximum) = minMax(arr)
  return (arr.index(minimum), arr.index(maximum))

class Sorter:
  NO_CARD = -1

  # region Functions
  def initPile(self, pileIndex, array = []):
    self.virtualTwinStacks[pileIndex].clear()
    self.virtualTwinStacks[pileIndex].extend(array)

  def bulkPeekValues(self, piles):
    tops = []
    for p in piles:
      if len(self.virtualTwinStacks[p]) > 0:
        tops.append(self.peek(p))
    self.population.bulkRegister(tops)
    cardRanks = []
    for p in piles:
      cardRanks.append(self.peekValue(p))
    return cardRanks

  def peek(self, pileIndex):
    if len(self.virtualTwinStacks[pileIndex]) <= 0:
      return Sorter.NO_CARD
    return self.virtualTwinStacks[pileIndex][-1]

  def peekValue(self, pileIndex):
    p = self.peek(pileIndex)
    if p  == Sorter.NO_CARD:
      return p 
    return self.population.getValue(p)

  def transfer(self, pileFrom, pileTo):
    if self.stop:
      return
    if len(self.virtualTwinStacks[pileFrom])<=0:
      raise Exception()
    name = self.virtualTwinStacks[pileFrom].pop()
    self.virtualTwinStacks[pileTo].append(name)

  def dealOut(self, dealFrom, sortInArray, lowestOnTop = False):
    if len(self.virtualTwinStacks[dealFrom])<=0:
      return (dealFrom, dealFrom)
    p = [dealFrom]
    p.extend(sortInArray)
    values = self.bulkPeekValues(p)
    sortInPileValues = values[1:]
    for i in range(len(sortInPileValues)):
      if lowestOnTop:
        if values[0] <= sortInPileValues[i] or sortInPileValues[i] == Sorter.NO_CARD:
          #self.transfer(dealFrom, sortInArray[i])
          return (dealFrom, sortInArray[i])
      else: 
        if values[0] >= sortInPileValues[i] or sortInPileValues[i] == Sorter.NO_CARD:
          #self.transfer(dealFrom, sortInArray[i])
          return (dealFrom, sortInArray[i])
    return (dealFrom, dealFrom)

  def collect(self, sortInArray, collectIn, collectLowestFirst = False):
    allEmpty = True
    for pile in sortInArray:
      if len(self.virtualTwinStacks[pile]) != 0:
        allEmpty = False
        break
    if allEmpty:
      return (collectIn, collectIn)
    
    p = [collectIn]
    p.extend(sortInArray)
    values = self.bulkPeekValues(p)
    sortInPileValues = values[1:]

    (minimumIndex, maximumIndex) = minMaxIndex(sortInPileValues)
    if collectLowestFirst:
      return(sortInArray[minimumIndex], collectIn)
    else:
      return(sortInArray[maximumIndex], collectIn)
  
  # endregion

  def __init__(self, numStacks):
    self.population = CardCompare()
    self.numStacks = numStacks
    # Pile sort
    self.virtualTwinStacks = []
    for i in range(self.numStacks):
      self.virtualTwinStacks.append([])
    
    if numStacks <= 3:
      raise Exception("Underconstrained sorting")
    
    self.dealFromPile = 0
    self.collectInPile = self.numStacks - 1
    self.sortingPiles = [item for item in range(1, self.numStacks - 1)]

    self.dealing = True
    self.stop = False
    self.endGame = False

  def getExpectedTopCard(self, pile_index):
    p = self.virtualTwinStacks[pile_index]
    if len(p) == 0:
      return None
    return p[-1]    

  def registerTopCardOfPile(self, pile_index, cardName):
    p = self.virtualTwinStacks[pile_index]
    if cardName is None:
      p.clear()
      return False
    registeredName = self.population.register(cardName)
    if len(p) == 0:
      p.append(registeredName)
      return True
    if self.getExpectedTopCard(pile_index) == registeredName:
      return True
    raise Exception("Unexpected Card")
  
  def flip(self):
    self.sortingPiles.reverse()
    (self.dealFromPile, self.collectInPile) = (self.collectInPile, self.dealFromPile)

  def suggestMove(self):
    transferSuggestion = (-1, -1)
    if self.stop:
      return transferSuggestion
    if len(self.virtualTwinStacks[self.dealFromPile]) == 0:
      if len(self.virtualTwinStacks[self.collectInPile]) == 0:
        self.endGame = True
    if self.dealing:
      transferSuggestion = self.dealOut(self.dealFromPile, self.sortingPiles)
    else: 
      transferSuggestion = self.collect(self.sortingPiles, self.collectInPile)
    if transferSuggestion[0] == transferSuggestion[1]:
      if not self.dealing and self.getExpectedTopCard(self.dealFromPile) is None:
        if self.endGame:
          self.stop = True
        else:
          self.flip()
      self.dealing = not self.dealing
      return self.suggestMove()
    return transferSuggestion



  # time_start = time()
  # shuffles = 1000
  # while shuffles > 1:
  #   shuffles = todoName(initial_pile, sorting_piles, last_pile)
  #   sorting_piles.reverse()
  #   (initial_pile, last_pile) = (last_pile, initial_pile)
  #   print(time()-time_start)


