import numpy as np
from membership_threshold import membership_threshold
from activity_threshold import activity_threshold

#Runs Monte-Carlo analysis to determine assembly membership and assembly activity
def monte_carlo_analysis(rot_seg_match,spt_mat,trig,N_rep,N_sig,time_window,cluster_list,dmr):
    sd,m,zscore_mat_shuf=membership_threshold(spt_mat,trig,N_rep,N_sig,time_window,cluster_list,dmr)
    #rot_seg_thresh_bin=assembly_composition(rot_seg_match,sd,m)
    activity_thresh=activity_threshold(rot_seg_match,zscore_mat_shuf)
    return activity_thresh
