from Card import Card
from CardCompare import CardCompare

cardNames = ["Azorius Charm","Boros Charm", "Gruul Charm",
             "Eye of Ugin", "Mountain", "Shadowborne Apostle",
             "Skullclamp", "Geist of Saint Traft", "Eerie Ultimatum",
             "Ramos, Dragon Engine", "Island", "Plains", "Wastes",
             "Piety Charm", "Colossal Dreadmaw",
             "Jungle Shrine", "Jetmir's Garden", "Savai Triome",
             "Wastes", "City of Brass", "Ornithopter", "Bone Saw",
             "Cromat", "Arbor Dryad", "Khalni Garden", "Command Tower",
             "Arcane Signet", "Selesnya Guildgate"]

cards = []
for c in cardNames:
    cards.append(Card(c))

repeatIsNecessary = True
iterations = 0
while repeatIsNecessary:
  repeatIsNecessary = False
  for i in range(len(cardNames) - 1):
      result = CardCompare.compare( cards[i], cards[i+1] )
      if result == CardCompare.SECOND:
          repeatIsNecessary = True
          tempCard = cards[i]
          cards[i] = cards[i+1]
          cards[i+1] = tempCard
      a = 1
  iterations += 1
for c in cards:
  print(c.name)
print(f'{iterations} iterations')

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