import scipy.io
import numpy as np
import os
import time

def run_matlab_cluster_strf(location,date,dmr,list_clu,path_trig,path_spikes):
    path_trig='../'+path_trig
    path_spikes='../'+path_spikes
    scipy.io.savemat('./matlab_strf/params_cluster.mat',mdict={'location':str(location),'date':str(date),'dmr':dmr,'list_clu':list_clu,'path_trig':path_trig,'path_spikes':path_spikes})
    os.system('matlab -nodesktop -nojvm -nosplash -r "cd matlab_strf; relay_cluster ;exit"')
    time.sleep(500)
    os.system('del ./matlab_strf/params_cluster.mat')
    print('Finished all cluster strfs for dmr '+str(dmr) +'and path '+str(path_spikes))
