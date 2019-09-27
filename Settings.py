import os
import datetime




data_pattern = 'YYYY-MM-DD hh:mm:ss'

path = r'C:\Users\ognev\Desktop\Proect\GIT\ManchkinCounter'

grp_path = 'groups'
plr_path = 'players'
log_path = 'log'

sys_grp = 'sys.pickle'

def WriteLog(text, name):
    with open(os.path.join(path, log_path, 'log.txt'), 'a') as log:
        log.append(f'[ {datetime.datetime().strftime(data_pattern)} ][ {name} ][ {text} ]')
