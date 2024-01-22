import abc
import json
from CardManage.Sorter import Sorter 

class MachineInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self, config_file_path):
        self.config = self.load_config(config_file_path)
        self.numStacks = int(self.readFromConfig('numStacks'))
        self.maxCardsPerStack = int(self.readFromConfig('maxCardsPerStack'))

        self.sorter = Sorter(self.numStacks)
        

    def load_config(self, config_file_path):
        with open(config_file_path, 'r') as file:
            config_data = json.load(file)
        return config_data
    
    @property
    @abc.abstractmethod
    def xPosition(self):
        pass
    
    @property
    @abc.abstractmethod
    def zPosition(self):
        pass
    
    @property
    @abc.abstractmethod
    def stackIndex(self):
        pass
    
    @abc.abstractmethod
    def initialize(self):
        pass
    
    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def takePicture(self):
        pass
    
    @abc.abstractmethod
    def move(self, stackIndex: int):
        pass
    
    @abc.abstractmethod
    def raw_move(self, x: float, z: float):
        pass

    def readFromConfig(self, param):
        return int(self.config['parameters'][param])
