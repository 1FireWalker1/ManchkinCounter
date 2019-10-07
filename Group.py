import pickle as pck

from Player import col
from Player import Style

from Settings import WriteLog

class Group:
    _l_players = []
    _amount = 0
    _name = ''

    def __init__(self, players, type='default'):
        self._l_players = players
        self._amount = len(players)
        if type == 'sys':
            self._name = 'sys'
            self._l_players = players
        else:
            name = 'sys'
            while name == 'sys':
                name = input('Input name of the group (except (sys)): ')
                if name != 'sys':
                    self._name = name
        WriteLog(f'Group ({self._name}) was created', __name__)

    def AddPlayer(self, pl):
        self._l_players.append(pl)
        WriteLog(f'Player ({pl._name} added to group ({self._name}))', __name__)

    def ListOfPlayers(self):
        for index, player in enumerate(self._l_players):
            buf = col.colours[player._colour]
            print(f'{index}) Name: {buf[0]+buf[1]}{player.GetName()}{Style.RESET_ALL}; Sex: {player.GetSex()}')
        print('\n')
        WriteLog(f'List of players group ({self._name})', __name__)

    def Serialise(self, type='default'):
        if type == 'sys':
            with open(r'groups\sys.pickle', 'wb') as f:
                pck.dump(self, f)
        else:
            with open(f'groups\{self._name}.pickle', 'wb') as f:
                pck.dump(self, f)
        WriteLog(f'Group ({self._name}) was serialised', __name__)
