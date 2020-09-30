import scipy.io
import numpy as np

def npy_to_mat_conversion(location,date,dmr,assembly_activity_ica,trig,time_window):
    N_assembly=assembly_activity_ica.shape[0]
    sp_times=[[] for a in range(N_assembly)]
    fs=24414.0625
    act_assemb_time=np.zeros_like(assembly_activity_ica.T)
    act_assemb_time[:,:]=-1
    first_t=np.amin(trig)/fs
    for a in range(N_assembly):
        for b in range(assembly_activity_ica.shape[1]):
            if assembly_activity_ica[a,b]!=0:
                act_assemb_time[b,a]=b*time_window
        sp_times[a].append(act_assemb_time[:,a][act_assemb_time[:,a]!=-1]+first_t)

    filename='./matlab_strf/'+str(date)+'_'+str(location)+'_'+str(dmr)+'_spikes.mat'
    scipy.io.savemat(filename, mdict={'st_clu':sp_times},oned_as='column')
