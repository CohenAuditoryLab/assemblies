import os
import numpy as np

def sort_dir(data_dir):
    cassius_dir=[]
    miyagi_dir=[]
    dirs=np.load('../../spikes_data_directories.npy')
    for dir in dirs:
        if dir[35:-37]=='MrCassius':
            cassius_dir.append(dir)
        else:
            miyagi_dir.append(dir)
    cassius_dir=np.array(cassius_dir)
    miyagi_dir=np.array(miyagi_dir)
    np.save('../../cassius_data_dir.npy',cassius_dir)
    np.save('../../miyagi_data_dir.npy',miyagi_dir)

if __name__ == '__main__':
    sort_dir('../../spikes_data_directories.npy')
