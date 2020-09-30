import numpy as np

def sparsity(rot_seg):
    N_neur=rot_seg.shape[1]
    sp_measure=[]
    for r in rot_seg:
        ratio=(np.sqrt(N_neur)-np.sum(np.abs(r)))/(np.sqrt(N_neur)-1)
        sp_measure.append(1-ratio)
    sp_measure=np.array(sp_measure)
    return sp_measure
