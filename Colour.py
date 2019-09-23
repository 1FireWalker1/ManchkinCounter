from colorama import Fore, Back, Style

class MyCol:
    colours = {
        'BLACK': [Back.WHITE, Fore.BLACK], 'RED': [Back.BLACK, Fore.RED],
        'GREEN': [Back.BLACK, Fore.GREEN], 'YELLOW': [Back.BLACK, Fore.YELLOW],
        'BLUE': [Back.BLACK, Fore.BLUE], 'MAGENTA': [Back.BLACK, Fore.MAGENTA],
        'CYAN': [Back.BLACK, Fore.CYAN], 'WHITE': [Back.BLACK, Fore.WHITE]
    }
    example = 'Available colors: '+ Back.WHITE + Fore.BLACK + 'BLACK, ' + Fore.RED + Back.BLACK + 'RED, '+Fore.GREEN + 'GREEN, ' + Fore.YELLOW + 'YELLOW, ' + Fore.BLUE + 'BLUE, '+Fore.MAGENTA + 'MAGENTA, ' + Fore.CYAN + 'CYAN, ' + Fore.WHITE + 'WHITE.'



'''
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''
