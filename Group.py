from Player import pck
from Player import col
from Player import Style

class Group:
    _l_players = []
    _amount = 0
    _name = ''

    def __init__(self, players, type='default'):
        self._l_players = players
        self._amount = len(players)
        if type == 'sys': self._name = 'sys'
        elif type == 'game': self._name = 'game'
        else:
            while name in ['sys', 'game']:
                name = input('Input name of the group (except (sys), (game)): ')
            self._name = name

    def ListOfPlayers(self):
        for index, player in enumerate(self._l_players):
            buf = col.colours[player._colour]
            print(f'{index}) Name: {buf[0]+buf[1]}{player.GetName()}{Style.RESET_ALL}; Sex: {player.GetSex()}')

    def Serialise(self, type='default'):
        if type == 'sys':
            with open(r'groups\sys.pickle', 'wb') as f:
                pck.dump(self, f)
        else:
            with open(f'groups\{self._name}.pickle', 'wb') as f:
                pck.dump(self, f)
