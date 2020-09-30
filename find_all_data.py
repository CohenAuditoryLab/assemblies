import numpy as np
import os

def find_all_data(path):
    l_sub=[x[0] for x in os.walk(path)]
    l_sub_select=[]
    for dir in l_sub:
        if os.path.exists(dir+'\spike_times_good_clust.mat') and 'KS2_7_AC' in dir:
            l_sub_select.append(dir)

    #    print(dir)
    #print(l_sub_select)
    np.save('../../spikes_data_directories.npy',np.array(l_sub_select))
    #return l_sub_select
    #
if __name__ == '__main__':
    find_all_data('I:\Parooa\Synapse\i\kiloSorted_DMR')
