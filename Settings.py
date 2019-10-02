import os
import datetime

data_pattern = '%Y-%m-%d | %H:%M:%S,%f'

path = r'C:\Users\ognev\Desktop\Proect\GIT\ManchkinCounter'

grp_path = 'groups'
plr_path = 'players'
log_path = 'log'

sys_grp = 'sys.pickle'

def WriteLog(text, name, type = 'default'):
    if type == 'sep':
        with open(os.path.join(path, log_path, f'log.txt'), 'a+') as log:
            log.write('=='*50 + '\n')
    else:
        with open(os.path.join(path, log_path, f'log.txt'), 'a+') as log:
            d = datetime.datetime.now()
            log.write(f'[ {d.strftime(data_pattern)} ][ {name} ] {text} \n')
