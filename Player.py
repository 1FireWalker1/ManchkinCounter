import colorama
from  colorama import Fore, Back, Style

class Player:
    __lvl = 1
    __bonus = 0
    __name = ''
    __sex = ''
    __colour = ''
    __colours = {
        'BLACK': [Back.WHITE, Fore.BLACK], 'RED': [Back.BLACK, Fore.RED],
        'GREEN': [Back.BLACK, Fore.GREEN], 'YELLOW': [Back.BLACK, Fore.YELLOW],
        'BLUE': [Back.BLACK, Fore.BLUE], 'MAGENTA': [Back.BLACK, Fore.MAGENTA],
        'CYAN': [Back.BLACK, Fore.CYAN], 'WHITE': [Back.BLACK, Fore.WHITE]
    }
    __example = 'Available colors: '+ Back.WHITE + Fore.BLACK + 'BLACK, ' + Fore.RED + Back.BLACK + 'RED, '+Fore.GREEN + 'GREEN, ' + Fore.YELLOW + 'YELLOW, ' + Fore.BLUE + 'BLUE, '+Fore.MAGENTA + 'MAGENTA, ' + Fore.CYAN + 'CYAN, ' + Fore.WHITE + 'WHITE.'


    def __str__(self):
        res = f'''
            Name: {''+ self.__colours[self.__colour][0] + self.__colours[self.__colour][1]}{self.__name}{'' + Fore.RESET + Back.RESET}
            Level: {self.__lvl}
            Bonus: {self.__bonus}
            Sex: {self.__sex}
        '''
        return res

    def __init__(self):
        colorama.init()
        self.__name = input('Input ur name: ')
        self.__sex = input('Input ur sex: ')
        while True:
            print(self.__example)
            colour = input('Choose ur color: ').upper()
            if colour in self.__colours:
                self.__colour = colour
                break
            else: print('Check available colours')

    def SetColor(self):
        while True:
            print(self.__example)
            colour = input('Choose ur color: ').upper()
            if colour in self.__colours:
                self.__colour = colour
                break
            else: print('Check available colours')

    def SetName(self):
        self.__name = input('Input ur new name: ')


'''
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''
