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

(0) Exit from Counter
'''

menu_edit_p ='''
(1) Edit name
(2) Edit Colour

(0) Exit from Editing
'''

action_main_menu = ['0', '1', '2', '3']
action_menu_edit_p = ['0', '1', '2']
