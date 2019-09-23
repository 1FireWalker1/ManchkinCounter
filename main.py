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
    print('Loading sys_group...', end = ' ')
    f = open(os.path.join(path, grp_path, sys_grp), 'rb')
    sys_group = pck.load(f)
    sys_group.ListOfPlayers()
    print('ok')
else:
    print('Creating sys_group...', end=' ')
    list_of_files_p = os.listdir(os.path.join(path, plr_path))
    if list_of_files_p is not None:
        for file in list_of_files_p:
            f = open(os.path.join(path, plr_path, file), 'rb')
            players.append(pck.load(os.path.join(path, plr_path, f)))
        sys_group = grp(players, 'sys')
        print('Ok')

for _ in range(2):
    p = plr()
    players.append(p)
    p.Serialise()


system_group = grp(players, 'sys')
sys_group.Serialise(type = 'sys')
