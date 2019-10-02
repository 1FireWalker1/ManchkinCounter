from Player import Player as plr
from Player import col
from Player import LoadingPlayers

from Group import Group as grp

from Settings import *

from Interface import PrintMenu, PrintMenuEditPlayer

import pickle as pck
import colorama
import os
import time

WriteLog('', __name__, 'sep')
WriteLog('Start of the program', __name__)
WriteLog('Colorama init...', __name__)
colorama.init()
WriteLog('Ok', __name__)

sys_group = LoadingPlayers()
sys_group.ListOfPlayers()

WriteLog('Additional players (?)', __name__)
ch = input('Do u want to create additional players? (1/0)\n')
WriteLog(f'Answer: {ch}', __name__)
if ch == '1':
    os.system('cls')
    WriteLog('How much players to create (?)', __name__)
    ch = int(input('How much players do u want to create? \n'))
    WriteLog(f'Amount: {ch}', __name__)
    for i in range(ch):
        os.system('cls')
        WriteLog(f'{i}/{ch}', __name__)
        print(f'Create: {i}/{ch}')
        p = plr()
        p.Serialise()
        sys_group.AddPlayer(p)

os.system('cls')
sys_group.ListOfPlayers()
WriteLog('Choice of players for game...', __name__)
index = input('Input index of players for game (minimum 2)(split by ,): ').replace(' ', '').split(',')
WriteLog(f'Indexes: {index}', __name__)

buf = []
for i in index:
    buf.append(sys_group._l_players[int(i)])

sys_group = grp(buf, 'sys')
sys_group.Serialise()
sys_group.ListOfPlayers()

PrintMenu()
WriteLog('Action from menu (?)', __name__)
ch = input('What r u want to do?\n')
WriteLog(f'Action: {ch}', __name__)
if ch == '0': pass
if ch == '1': pass
if ch == '2':
    WriteLog('Editing Menu', __name__)
    os.system('cls')
    PrintMenuEditPlayer()
    WriteLog('Action from Editing Menu (?)', __name__)
    ch = input('What r u want to do?\n')
    WriteLog(f'Action: {ch}', __name__)
    if ch == '1':
        os.system('cls')
        sys_group.ListOfPlayers()
        WriteLog('Choice of player for Editing...', __name__)
        index = int(input('Input index of player for Editing: '))
        WriteLog(f'Index: {index}', __name__)
        sys_group._l_players[index].SetName()

if ch == '3': pass


WriteLog('Exit from program code: 0', __name__)
WriteLog('', __name__, 'sep')
