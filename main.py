from Player import Player as plr
from Player import col
from Player import pck

from Group import Group as grp

from Settings import *

import colorama
import os

colorama.init()
players = []

print('Loading players...', end = ' ')
WriteLog('Loading players...', __name__)
list_of_files_p = os.listdir(os.path.join(path, plr_path))
if list_of_files_p != []:
    for file in list_of_files_p:
        f = open(os.path.join(path, plr_path, file), 'rb')
        players.append(pck.load(os.path.join(path, plr_path, file), f))
        f.close()
    print('Ok')
    print('='*50 + '\n Available players:\n')
    sys_group = grp(players, 'sys')
    sys_group.ListOfPlayers()
else:
    print('List of players is empty...\n')
    amount = int(input('How much players do u want to create? '))
    if amount !=
        for i in range(int(amount)):
            p = plr()
            p.Serialise()
            pl.append(p)

# pl = []
# for _ in range(3):
#     p = plr()
#     p.Serialise()
#     pl.append(p)
#
# sys_group = grp(pl, 'sys')

# sys_group.Serialise(type = 'sys')
# sys_group.ListOfPlayers()
