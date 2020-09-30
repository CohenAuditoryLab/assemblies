import numpy as np
import time

#Computes assembly trajectory
def trajectories(expl_var,assembly_activity_ica_thresh,time_window,bin_window):
    ratio_dt=bin_window/time_window
    if assembly_activity_ica_thresh.shape[0]<3:
        N_dims= assembly_activity_ica_thresh.shape[0]
    else:
        N_dims=3
    act_assembly_ica_trunc=assembly_activity_ica_thresh[0:N_dims]
    N_bins_2=int(act_assembly_ica_trunc.shape[1]/ratio_dt)+1
    act_assembly_ica_binned=np.zeros((N_dims,N_bins_2))
    for a in range(N_dims):
        for b in range(act_assembly_ica_trunc.shape[1]):
            ind_bin=int(b/ratio_dt)
            act_assembly_ica_binned[a,ind_bin]+=act_assembly_ica_trunc[a,b]
    return act_assembly_ica_binned
