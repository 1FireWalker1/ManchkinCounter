from Player import Player as plr
from Player import col
from Player import pck

from Group import Group as grp

from Settings import *

import colorama
import os

colorama.init()
players = []

if os.path.isfile(os.path.join(path, grp_path, sys_grp)):
    print('Loading sys_group...')
    f = open(os.path.join(path, grp_path, sys_grp), 'rb')
    sys_group = pck.load(f)
    f.close()
    sys_group.ListOfPlayers()
else:
    print('Creating sys_group...')
    list_of_files_p = os.listdir(os.path.join(path, plr_path))
    if list_of_files_p != []:
        for file in list_of_files_p:
            f = open(os.path.join(path, plr_path, file), 'rb')
            players.append(pck.load(os.path.join(path, plr_path, file), f))
            f.close()
        sys_group = grp(players, 'sys')
        sys_group.ListOfPlayers()
    else:
        amount = int(input('How much players do u want to create? '))
        if amount !=
        for i in range(int(amount)):


# pl = []
# for _ in range(3):
#     p = plr()
#     p.Serialise()
#     pl.append(p)
#
# sys_group = grp(pl, 'sys')

# sys_group.Serialise(type = 'sys')
# sys_group.ListOfPlayers()
