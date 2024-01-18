from Card import Card
from CardCompare import CardCompare

population = CardCompare()

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
    population.getValue(c)

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