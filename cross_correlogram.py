import matplotlib.pyplot as plt
import numpy as np

# Returns the correlogram plot of clusters ind_cli_1 and ind_clu_2
def cross_correlogram(spike_mat,ind_clu_1,ind_clu_2,ftsize=22):
    gs=plt.GridSpec(40,20)
    plt.subplot(gs[0:6,10:14])
    plt.title('Cc-gram, clusters '+str(ind_clu_1)+' and '+str(ind_clu_2),fontsize=ftsize)
    plt.xcorr(spike_mat[ind_clu_1,:],spike_mat[ind_clu_2,:],normed=True)
    plt.xlabel('dt (ms)',fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
