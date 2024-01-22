from MachineManage.Machine import Machine
from MachineManage.MachineInterface import MachineInterface
from MachineManage.MachineSimulated import MachineSimulated

FULL_SIMULATION = True
CONFIG_FILE = 'MachineManage\\config.json'

machineController: MachineInterface

if FULL_SIMULATION:
    machineController = MachineSimulated(CONFIG_FILE)
else:
    machineController = Machine(CONFIG_FILE)

def main():
    print(machineController.x_position)
    

if __name__ == "__main__":
    main()