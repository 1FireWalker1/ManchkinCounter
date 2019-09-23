from  colorama import Fore, Back, Style
from Colour import MyCol as col
import pickle as pck

class Player:
    __lvl = 1
    __bonus = 0
    __name = ''
    __sex = ''
    __colour = ''

    def __init__(self):
        self.__name = input('Input ur name (Only letters): ')
        self.__sex = input('Input ur sex: ')
        while True:
            print(col.example)
            colour = input('Choose ur color: ').upper()
            if colour in col.colours:
                self.__colour = colour
                break
            else:
                print('Check available colours')

    def SetName(self):
        self.__name = input('Input ur new name (Only letters): ')

    def SetColor(self):
        while True:
            print(col.example)
            colour = input('Choose ur color: ').upper()
            if colour in col.colours:
                self.__colour = colour
                break
            else: print('Check available colours')

    def PrintInfo(self, col):
        print(f'''
            Name: {''+ col.colours[self.__colour][0] + col.colours[self.__colour][1]}{self.__name}{'' + Style.RESET_ALL}
            Level: {self.__lvl}
            Bonus: {self.__bonus}
            Sex: {self.__sex}
        ''')

    def Serialise(self):
        with open(f'players\{self.__name}.pickle', 'wb') as f:
            pck.dump(self, f)
