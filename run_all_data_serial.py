import numpy as np
import os
from find_all_data import  find_all_data
from analyse_real_data import analyse_real_data
import time

def run_all_data_serial(monkey,time_window=0.01):
    #path='I:\Parooa\Synapse\i\kiloSorted_DMR'
    #dirs=find_all_data(path)
    #prefix=path+'Cassius-'
    #suffix='/select_clu.npy'

    #print(dirs)
    shuffled=False
    montecarlo_analysis=True
    date=''
    location=''
    list_data=[]
    variance_var=[]
    if monkey=='cassius':
        dirs=np.load('../../cassius/cassius_data_dir.npy')
    elif monkey=='miyagi':
        dirs=np.load('../../miyagi/miyagi_data_dir.npy')

    for d,i in zip(dirs,range(len(dirs))):

        #cluster_list=np.load(d+'/select_clu.npy')
        cluster_list=None
        #info_data=d[len(prefix):]
        #print('b:'+info_data)
        #list_data.append(info_data)
        #date=info_data[0:6]

        date=d[-36:-30]
        #print('a:'+date)

        #if len(info_data)>6:
        #    location=info_data[7:]
        if monkey=='cassius':
            location=d[52:-21]
        else:
            location=d[51:-21]
        print('date: '+str(date))
        print('location: '+str(location))
        variance_var.append(analyse_real_data(d,date,location,time_window,cluster_list,1,shuffled,montecarlo_analysis,'off'))
        variance_var.append(analyse_real_data(d,date,location,time_window,cluster_list,2,shuffled,montecarlo_analysis,'off'))

    np.save('../../'+str(monkey)+'/'+str(monkey)+'_data_serial_mc2_'+str(montecarlo_analysis)+'_'+str(time_window),np.array(variance_var))

if __name__ == '__main__':

    t0 = time.time()
    run_all_data_serial('cassius',0.01)
    t1 = time.time()
    delta_t=t1-t0
    print('Total time: '+str(delta_t)+' s')
