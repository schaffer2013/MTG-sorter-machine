from CardManage.Card import Card
from CardManage.CardCompare import CardCompare
from CardManage.Sorter import Sorter

s = Sorter (5)

print(s.sortingPiles)

cardNames = ["Azorius Charm","Boros Charm", "Gruul Charm",
             "Eye of Ugin", "Mountain", "Shadowborne Apostle",
             "Skullclamp", "Geist of Saint Traft", "Eerie Ultimatum",
             "Ramos, Dragon Engine", "Island", "Plains", "Wastes",
             "Piety Charm", "Colossal Dreadmaw", "The Kami War"]#,
            # "Jungle Shrine", "Jetmir's Garden", "Savai Triome",
            #  "Wastes", "City of Brass", "Ornithopter", "Squirrel", "Bone Saw",
            #  "Cromat", "Clue", "Dryad Arbor", "Khalni Garden", "Command Tower",
            #  "Arcane Signet", "Selesnya Guildgate"]

index = 0
cardNameLen = len(cardNames)

while (index < cardNameLen):
    s.registerTopCardOfPile(0, cardNames[index])
    a = s.suggestMove()
    s.transfer(a[0], a[1])
    if a[0] == 0:
        index += 1

stillSorting = False
for p in s.virtualTwinStacks:
    if len(p) > 0:
        stillSorting = True
while (stillSorting == True and not s.stop):
    for p in s.virtualTwinStacks:
        if len(p) > 0:
            stillSorting = True
            break
    a = s.suggestMove()
    s.transfer(a[0], a[1])
s.suggestMove()