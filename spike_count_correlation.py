import numpy as np
import matplotlib.pyplot as plt

#Plots spike count of clu_1 as a function of clu_2 at a specific time bin
def spike_count_correlation(spike_mat,ind_clu_1,ind_clu_2,ftsize=22):
    gs=plt.GridSpec(40,20)
    plt.subplot(gs[0:6,15:19])
    plt.scatter(x=spike_mat[ind_clu_1,:],y=spike_mat[ind_clu_2,:],s=40,color='#ff7f0e')
    plt.xlabel('Spike count, cluster '+str(ind_clu_1),fontsize=ftsize)
    plt.ylabel('Spike count, cluster '+str(ind_clu_2),fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
