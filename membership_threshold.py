import numpy as np
from spike_matrix import spike_matrix
from z_scoring import z_scoring
from cov_matrix import cov_matrix
from assembly_detection_shuf import assembly_detection_shuf
#Determine significance threshold for assembly membership
def membership_threshold(spt_mat,trig,N_rep,N_sig,time_window,cluster_list,dmr):
    dist_weights=[]
    sp_mat_shuf=[]
    for r in range(N_rep):
        spike_mat=spike_matrix(spt_mat,trig,time_window,cluster_list,dmr,True)
        zscore_mat=z_scoring(spike_mat,cluster_list)
        sp_mat_shuf.append(zscore_mat)
        cov_mat=cov_matrix(zscore_mat,cluster_list)
        weights_IC_flat=assembly_detection_shuf(zscore_mat,N_sig)
        dist_weights.append(weights_IC_flat)
    dist_weights=np.array(dist_weights).flatten()
    m=np.mean(dist_weights)
    sd=np.std(dist_weights)
    sp_mat_shuf=np.array(sp_mat_shuf)

    return sd,m,sp_mat_shuf
