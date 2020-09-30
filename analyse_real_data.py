import numpy as np
from load_spike_times import load_spike_times
from load_triggers import load_triggers
from spike_matrix import spike_matrix
from raster_plot import raster_plot
from z_scoring import z_scoring
from cov_matrix import cov_matrix
from assembly_detection import assembly_detection
from neuronal_participation import neuronal_participation
from assembly_matching import assembly_matching
from projected_activity import projected_activity
from monte_carlo_analysis import monte_carlo_analysis
from spike_matrix_assembly import spike_matrix_assembly
from trajectories import trajectories
from variance_decrease import variance_decrease
from npy_to_mat_conversion import npy_to_mat_conversion
from run_matlab_cluster_strf import run_matlab_cluster_strf
from run_matlab_assembly_strf import run_matlab_assembly_strf
from sparsity import sparsity
from word_collection import word_collection
from firing_rate import firing_rate
from firing_rate_assemblies import  firing_rate_assemblies

def analyse_real_data(path,date,location,time_window,cluster_list,dmr,shuffled,montecarlo_analysis,multithread='on',procnum=0,return_dict=None):

    spt_mat,path_spikes=load_spike_times(path)
    trig,path_trig=load_triggers(path,dmr)
    if spt_mat is not None:
        spike_mat=spike_matrix(spt_mat,trig,time_window,cluster_list,dmr,shuffled)
        fir_rate=firing_rate(spike_mat)
        zscore_mat=z_scoring(spike_mat)
        cov_mat=cov_matrix(zscore_mat,cluster_list)
        sig_eig_vec,bel_lam_min_vec,expl_var=assembly_detection(path,dmr,zscore_mat)
        if cluster_list is None:
            N_neur=spt_mat.shape[0]
        else:
            N_neur=len(cluster_list)
        if len(sig_eig_vec)!=0:
            N_sig=sig_eig_vec.shape[0]
            z,variance_explained_N_sig,euc_norm,var_decrease=variance_decrease(path,dmr,zscore_mat,N_sig)
            rot_seg=neuronal_participation(zscore_mat,sig_eig_vec)
            rot_seg_match=assembly_matching(sig_eig_vec,rot_seg)
            sparsity_measure=sparsity(rot_seg_match)
            assembly_activity_pca,assembly_activity_ica=projected_activity(zscore_mat,sig_eig_vec,rot_seg_match)

            if montecarlo_analysis:
                N_rep=30
                activity_thresh=monte_carlo_analysis(rot_seg_match,spt_mat,trig,N_rep,N_sig,time_window,cluster_list,dmr)
                time_assembly_ica,assembly_activity_ica_thresh=spike_matrix_assembly(activity_thresh,assembly_activity_ica,time_window)
                fir_rate_assemblies=firing_rate_assemblies(assembly_activity_ica_thresh)
                #word_collection(assembly_activity_ica_thresh,time_window,8,shuffle=True)
                #bin_window=1
                #npy_to_mat_conversion(location,date,dmr,assembly_activity_ica,trig,time_window)
                #run_matlab_cluster_strf(location,date,dmr,cluster_list,path_trig,path_spikes)
                #run_matlab_assembly_strf(N_sig,location,date,dmr,path_trig,path_spikes,time_window)
                #act_assembly_ica_binned=trajectories(expl_var,assembly_activity_ica_thresh,time_window,bin_window)

            if multithread=='on':
                return_dict[procnum]=(N_sig,z,variance_explained_N_sig,N_neur,euc_norm,var_decrease,date,location,dmr,procnum,cluster_list,rot_seg_match,fir_rate,fir_rate_assemblies,sparsity_measure,assembly_activity_ica_thresh)
            else:
                return (N_sig,z,variance_explained_N_sig,N_neur,euc_norm,var_decrease,date,location,dmr,procnum,cluster_list,rot_seg_match,fir_rate,fir_rate_assemblies,sparsity_measure,assembly_activity_ica_thresh)

        else:
            if multithread=='on':
                return_dict[procnum]=(0,-1,0,N_neur,-1,-1,date,location,dmr,procnum,cluster_list,[],fir_rate,[],-1,[])
            else:
                return (0,-1,0,N_neur,-1,-1,date,location,dmr,procnum,cluster_list,[],fir_rate,[],-1,[])






if __name__ == '__main__':
    analyse_real_data('../data_Lalitta/Cassius-190326',0.01,'bla',1,False,True)
