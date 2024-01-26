from CardManage.Card import Card
from MachineManage.MachineInterface import MachineInterface
from PIL import Image
import requests
from io import BytesIO

import random

cardNames = ["Azorius Charm","Boros Charm", "Gruul Charm",
             "Eye of Ugin", "Mountain", "Shadowborne Apostle",
             "Skullclamp", "Geist of Saint Traft", "Eerie Ultimatum",
             "Ramos, Dragon Engine", "Island", "Plains", "Wastes",
             "Piety Charm", "Colossal Dreadmaw", "The Kami War",
             "Jungle Shrine", "Jetmir's Garden", "Savai Triome",
             "Wastes", "City of Brass", "Ornithopter", "Squirrel", "Bone Saw",
             "Cromat", "Clue", "Dryad Arbor", "Khalni Garden", "Command Tower",
             "Arcane Signet", "Selesnya Guildgate"]

class MachineSimulated(MachineInterface):
    def __init__(self, config_file_path):
        super(MachineSimulated, self).__init__(config_file_path)
        self.x_position = random.uniform(0.0, 10.0)
        self.z_position = random.uniform(0.0, 1.0)
        self.current_stack_index = -1
    
    def initialize(self):
        # Implement the initialization logic specific to your machine
        self.sorter.initPile(0, array = cardNames)
        self.move(0)
    
    def connect(self):
        # Implement the connection logic specific to your machine
        pass

    def takePicture(self):
        if self.current_stack_index in range(self.numStacks + 1):
            topCard = self.sorter.getExpectedTopCard(self.current_stack_index)
            if topCard == None:
                return
            img = self.getCardImage(topCard)
            return img
        pass
    
    def move(self, pile_index: int):
        self.current_stack_index = pile_index
        # Implement the movement logic specific to your machine
        pass
    
    def raw_move(self, x: float, z: float):
        # Implement the raw movement logic specific to your machine
        pass
    
    @property
    def xPosition(self):
        # Implement the getter for xPosition property
        return self.x_position
    
    @property
    def zPosition(self):
        # Implement the getter for zPosition property
        return self.z_position
    
    @property
    def stackIndex(self):
        # Implement the getter for stackIndex property
        return self.current_stack_index
    
    def getCardImage(self, name):
        card = Card(name)
        response = requests.get(card.url)
        img = Image.open(BytesIO(response.content))
        return img