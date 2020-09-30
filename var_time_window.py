import numpy as np
from run_all_data import run_all_data
import time
def var_time_window():
    time_window=[0.05]#[0.005,0.01,0.02,0.1]
    for t in time_window:
        run_all_data(t)
    print('Finished varying time window')

if __name__ == '__main__':
    t0 = time.time()
    var_time_window()
    t1 = time.time()
    delta_t=t1-t0
    print('Total time: '+str(delta_t)+' s')
