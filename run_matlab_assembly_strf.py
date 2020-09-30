import numpy as np
import scipy.io
import os
from pathlib import Path
import time

def run_matlab_assembly_strf(N_assembly,location,date,dmr,path_trig,path_spikes,time_window):

    path_trig='../'+path_trig
    path_spikes='../'+path_spikes
    scipy.io.savemat('./matlab_strf/params_assembly.mat',mdict={'location':location,'date':date,'dmr':dmr,'N_assembly':N_assembly,'path_trig':path_trig,'path_spikes':path_spikes,'time_window':time_window})
    os.system('matlab -nodesktop -nojvm -nosplash -r "cd matlab_strf ; relay_assembly ; exit"')
    time.sleep(250)
    os.system('del ./matlab_strf/params_assembly.mat')
