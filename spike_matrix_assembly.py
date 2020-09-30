import numpy as np


#Thresholds assembly activity
def spike_matrix_assembly(activity_thresh,assembly_activity_ica,time_window):
    assembly_activity_ica[assembly_activity_ica<=activity_thresh]=0.0
    assembly_activity_ica[assembly_activity_ica>activity_thresh]=1.0
    N_assembly=assembly_activity_ica.shape[0]
    N_bins=assembly_activity_ica.shape[1]
    time_assembly_ica=np.zeros_like(assembly_activity_ica)
    for a in range(N_assembly):
        for b in range(N_bins):
            if assembly_activity_ica[a,b]>activity_thresh:
                time_assembly_ica[a,b]=b*time_window

    return time_assembly_ica,assembly_activity_ica
