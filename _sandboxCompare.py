import random
from time import sleep, time

import scrython
from Card import Card
from CardCompare import CardCompare

NO_CARD = 999999
pre_time = time()

def initPile(pileIndex, array = []):
  allPiles[pileIndex].clear()
  allPiles[pileIndex].extend(array)

def bulkPeekValues(piles):
  tops = []
  for p in piles:
    if len(allPiles[p]) > 0:
      tops.append(peek(p))
  population.bulkRegister(tops)
  cardRanks = []
  for p in piles:
    cardRanks.append(peekValue(p))
  return cardRanks

def peek(pileIndex):
  if len(allPiles[pileIndex]) <= 0:
    return NO_CARD
  return allPiles[pileIndex][-1]

def peekValue(pileIndex):
  p = peek(pileIndex)
  if p  == NO_CARD:
    return p 
  return population.getValue(p)

def transfer(pileFrom, pileTo):
  if len(allPiles[pileFrom])<=0:
    raise Exception()
  name = allPiles[pileFrom].pop()
  allPiles[pileTo].append(name)
  #totalMoves += 1

def todoName(dealFrom, sortInArray, collectIn, standardOrder = True):
  shuffles = 0
  while len(allPiles[dealFrom])>0:
    # Deal out
    dealt = True
    while dealt:
      dealt = dealOut(dealFrom, sortInArray, standardOrder)
    # Collect
    collected = True
    while collected:
      collected = collect(sortInArray, collectIn, standardOrder)
    shuffles += 1
  print(shuffles)
  return shuffles

def dealOut(dealFrom, sortInArray, lowestOnTop = True):
  if len(allPiles[dealFrom])<=0:
    return
  p = [dealFrom]
  p.extend(sortInArray)
  values = bulkPeekValues(p)
  sortInPileValues = values[1:]
  for i in range(len(sortInPileValues)):
    if lowestOnTop:
      if values[0] <= sortInPileValues[i] or sortInPileValues[i] == NO_CARD:
        transfer(dealFrom, sortInArray[i])
        return True
    else: 
      if values[0] >= sortInPileValues[i] or sortInPileValues[i] == NO_CARD:
        transfer(dealFrom, sortInArray[i])
        return True
  return False
  

def collect(sortInArray, collectIn, collectLowestFirst = True):
  allEmpty = True
  for pile in sortInArray:
    if len(allPiles[pile]) != 0:
      allEmpty = False
      break
  if allEmpty:
    return False
  
  p = [collectIn]
  p.extend(sortInArray)
  values = bulkPeekValues(p)
  sortInPileValues = values[1:]

  (minimumIndex, maximumIndex) = minMaxIndex(sortInPileValues)
  if collectLowestFirst:
    transfer(sortInArray[minimumIndex], collectIn)
  else:
    transfer(sortInArray[maximumIndex], collectIn)
  return True

def minMax(arr):
  min = 100000000
  max = -min
  for a in arr:
    if a < min and a != NO_CARD:
      min = a
    if a > max and a != NO_CARD:
      max = a
  return (min, max)

def minMaxIndex(arr):
  (minimum, maximum) = minMax(arr)
  return (arr.index(minimum), arr.index(maximum))

population = CardCompare()

NUM_CARDS = 300

cardNames = []
for i in range(NUM_CARDS):
  cardNames.append(scrython.cards.Random().name())
  sleep(0.01)

# cardNames = ["Azorius Charm","Boros Charm", "Gruul Charm",
#              "Eye of Ugin", "Mountain", "Shadowborne Apostle",
#              "Skullclamp", "Geist of Saint Traft", "Eerie Ultimatum",
#              "Ramos, Dragon Engine", "Island", "Plains", "Wastes",
#              "Piety Charm", "Colossal Dreadmaw", "The Kami War",
#              "Jungle Shrine", "Jetmir's Garden", "Savai Triome",
#              "Wastes", "City of Brass", "Ornithopter", "Squirrel", "Bone Saw",
#              "Cromat", "Clue", "Dryad Arbor", "Khalni Garden", "Command Tower",
#              "Arcane Signet", "Selesnya Guildgate"]


random.shuffle(cardNames)

# Pile sort
NUM_PILES = 5
allPiles = []
for i in range(NUM_PILES):
  allPiles.append([])

totalMoves = 0

initPile(0, cardNames)

initial_pile = 0
sorting_piles = [1, 2, 3]
last_pile = 4

print(f'Pre-time: {time() - pre_time}')

time_start = time()
shuffles = 1000
while shuffles > 1:
  shuffles = todoName(initial_pile, sorting_piles, last_pile)
  sorting_piles.reverse()
  (initial_pile, last_pile) = (last_pile, initial_pile)
  print(time()-time_start)


for c in population._populationNames:
  print(c)


# Should print:
# Piety Charm
# Shadowborn Apostle
# Colossal Dreadmaw
# Azorius Charm
# Geist of Saint Traft
# Boros Charm
# Gruul Charm
# Eerie Ultimatum
# Cromat
# Bone Saw
# Ornithopter
# Skullclamp
# Arcane Signet
# Ramos, Dragon Engine
# Dryad Arbor
# Khalni Garden
# Selesnya Guildgate
# Savai Triome
# Jetmir's Garden
# Jungle Shrine
# City of Brass
# Command Tower
# Eye of Ugin
# Plains
# Island
# Mountain
# Wastes
# Wastes