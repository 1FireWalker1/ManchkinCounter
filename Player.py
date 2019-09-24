from  colorama import Fore, Back, Style
from Colour import MyCol as col

from Settings import  *

import pickle as pck
import os

class Player:
    _lvl = 1
    _bonus = 0
    _name = ''
    _sex = ''
    _colour = ''

    def __init__(self):
        os.system('cls')
        name = ''
        while os.path.join(path, plr_path, name.join('.pickle')) in os.listdir(os.path.join(path, plr_path)) or name == '':
            name = input('Input ur name (Only letters): ')
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


    def SetName(self):
        self._name = input('Input ur new name (Only letters): ')

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
