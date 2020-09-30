import numpy as np
import os
from find_all_data import  find_all_data
from analyse_real_data import analyse_real_data
from multiprocessing import Process, Manager
import time

def run_all_data_parallel(time_window=0.01):
    path='../data_Lalitta/'
    dirs=find_all_data(path)
    prefix=path+'Cassius-'
    suffix='/select_clu.npy'

    #print(dirs)
    shuffled=False
    montecarlo_analysis=False
    manager = Manager()
    return_dict = manager.dict()
    processes_1=[]
    processes_2=[]

    #info_data=[]
    date=''
    location=''
    list_data=[]

    for d,i in zip(dirs,range(len(dirs))):
        cluster_list=np.load(d+'/select_clu.npy')
        info_data=d[len(prefix):]
        print('b:'+info_data)
        list_data.append(info_data)
        date=info_data[0:6]
        #print('a:'+date)

        if len(info_data)>6:
            location=info_data[7:]
        else:
            location=''
        processes_1.append(Process(target=analyse_real_data, args=(d,date,location,time_window,cluster_list,1,shuffled,montecarlo_analysis,'on',2*i,return_dict,)))
        processes_2.append(Process(target=analyse_real_data, args=(d,date,location,time_window,cluster_list,2,shuffled,montecarlo_analysis,'on',2*i+1,return_dict,)))
    for p1 in processes_1:
        p1.start()
    for p2 in processes_2:
        p2.start()

    for p1 in processes_1:
        p1.join()
    for p2 in processes_2:
        p2.join()

    np.save('variance_var_'+str(time_window),return_dict.values())
if __name__ == '__main__':

    t0 = time.time()
    run_all_data_parallel(0.005)
    t1 = time.time()
    delta_t=t1-t0
    print('Total time: '+str(delta_t)+' s')
