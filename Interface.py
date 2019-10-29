from Settings import WriteLog

def PrintMenu():
    print(main_menu)
    WriteLog('Call main Menu', __name__)

def PrintMenuEditPlayer():
    print(menu_edit_p)
    WriteLog('Call Edit Menu', __name__)

main_menu = '''
(1) Start Game
(2) Edit Player
(3) Delete Player

(!) Exit from Counter
'''

menu_edit_p ='''
(1) Edit name
(2) Edit Colour

(!) Exit from Editing
'''

menu_game = '''
(1) Add Level +1
(2) Sub Level -1
(3) Add Gear +1
(4) Sub Gear -1

(!) Back
'''

action_main_menu = ['!', '1', '2', '3']
action_menu_edit_p = ['!', '1', '2']
action_menu_game = ['!', '1', '2', '3', '4']
