import os
import numpy as np

def find_triggers(trigger_path,data_path):
    monkey=data_path[35:-37]
    if monkey=='MrCassius':
        trigger_path=trigger_path+'/Cassius'
    else:
        trigger_path=trigger_path+'/Miyagi'
    for filename in os.listdir(trigger_path):
        if data_path[-36:-30] in filename:
            #print(filename)
            return trigger_path+'/'+filename

if __name__ == '__main__':
    find_triggers( 'I:\Parooa\Synapse\i\kiloSorted_DMR\Triggers','I:\\Parooa\\Synapse\\i\\kiloSorted_DMR\\MrMiyagi-190817\\D4_AC_R1\\KS2_7_AC\\ClusterInfo',)
