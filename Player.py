from  colorama import Fore, Back, Style
from Colour import MyCol as col

from Settings import *

from Group import Group as grp


import os
import pickle as pck

def LoadingPlayers():
    players = []
    WriteLog('Loading players...', __name__)
    list_of_files_p = os.listdir(os.path.join(path, plr_path))
    if list_of_files_p != []:
        for file in list_of_files_p:
            WriteLog(f"Loading player ({file.split('.')[0]}) ...", __name__)
            f = open(os.path.join(path, plr_path, file), 'rb')
            players.append(pck.load(f))
            f.close()
            WriteLog('Ok (Loading player)', __name__)
        WriteLog('Ok', __name__)
        print('='*50 + '\nAvailable players in system:\n')
        return grp(players, 'sys')
    else:
        WriteLog('Empty list of saved players occured, start creating', __name__)
        print('List of players is empty...\n')
        WriteLog('How much players to create (?)', __name__)
        amount = int(input('How much players do u want to create? \n'))
        WriteLog(f'Amount: {amount}', __name__)
        for i in range(int(amount)):
            os.system('cls')
            WriteLog(f'{i}/{amount}', __name__)
            print(f'Create: {i}/{amount}')
            p = Player()
            p.Serialise()
            players.append(p)
        WriteLog('Ok', __name__)
        return grp(players, 'start')

class Player:
    _lvl = 1
    _bonus = 0
    _name = ''
    _sex = ''
    _colour = ''

    def __init__(self):
        name = ''
        while os.path.join(path, plr_path, name + '.pickle') in os.listdir(os.path.join(path, plr_path)) or name == '':
            name = input('Input ur name (Only letters and numbers): ')
            self._name = name

        self._sex = input('Input ur sex: ')
        while True:
            print(col.example)
            colour = input('Choose ur color: ').upper()
            if colour in col.colours:
                self._colour = colour
                break
            else:
                print('Check available colours')
        os.system('cls')
        WriteLog(f'Player ({self._name}) was created', __name__)

    def Delete(self):
        os.remove(os.path.join(path, plr_path, self._name + '.pickle'))
        WriteLog(f'Player ({self._name}) deleted', __name__)

    def SetName(self):
        name = input('Input ur new name (Only letters and numbers): ')
        os.remove(os.path.join(path, plr_path, self._name + '.pickle'))
        WriteLog(f'Player ({self._name}): set Name from ({self._name}) --> ({name})', __name__)
        self._name = name
        self.Serialise()

    def GetName(self):
        return self._name

    def GetSex(self):
        return self._sex

    def SetColor(self):
        os.system('cls')
        while True:
            print(col.example)
            colour = input('Choose ur color: ').upper()
            if colour in col.colours:
                self._colour = colour
                break
            else:
                print('Check available colours')
        os.system('cls')

    def PrintInfo(self, col):
        print(f'''
            Name: {''+ col.colours[self._colour][0] + col.colours[self._colour][1]}{self.GetName()}{'' + Style.RESET_ALL}
            Level: {self._lvl}
            Bonus: {self._bonus}
            Sex: {self.GetSex()}
        ''')

    def Serialise(self):
        with open(f'players\{self._name}.pickle', 'wb') as f:
            pck.dump(self, f)

        WriteLog(f'Player ({self._name}) was serialised', __name__)
