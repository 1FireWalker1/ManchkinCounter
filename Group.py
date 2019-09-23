from Player import pck

class Group:
    __l_players = []
    __amount = 0
    __name = ''

    def __init__(self, players, type='default'):
        self.__l_players = players
        self.__amount = len(players)
        if type == 'sys': self.__name = 'sys'
        elif type == 'game': self.__name = 'game'
        else:
            while name in ['sys', 'game']:
                name = input('Input name of the group (except (sys), (game)): ')
            self.__name = name

    def ListOfPlayers(self):
        for index, player in enumerate(self.__l_players):
            print(list(enumerate(self.__l_players)))
            print(f'{index}) Name: {player.__name}; Sex: {player.__sex}')

    def Serialise(self, type='default'):
        if type == 'sys':
            with open(r'groups\sys.pickle', 'wb') as f:
                pck.dump(self, f)
        else:
            with open(f'groups\{self.__name}.pickle', 'wb') as f:
                pck.dump(self, f)
