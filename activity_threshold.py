import numpy as np

#Determines threshold for assembly activity
def activity_threshold(rot_seg_thresh,sp_mat_shuf):
    N_assembly=rot_seg_thresh.shape[0]
    N_bins=sp_mat_shuf.shape[2]
    N_rep=sp_mat_shuf.shape[0]
    activity_values=np.zeros((N_rep,N_assembly,N_bins))
    for n in range(N_rep):
        for a in range(N_assembly):
            for b in range(N_bins):
                assembly_pattern_ica=np.outer(rot_seg_thresh[a,:],rot_seg_thresh[a,:])
                np.fill_diagonal(assembly_pattern_ica, 0)
                proj_ica=np.matmul(sp_mat_shuf[n,:,b].T,assembly_pattern_ica)
                activity_values[n,a,b]=np.matmul(proj_ica,sp_mat_shuf[n,:,b])
    activity_values=np.array(activity_values).flatten()
    thresh_perc=99.9
    pc=np.percentile(activity_values,thresh_perc)
    return pc
