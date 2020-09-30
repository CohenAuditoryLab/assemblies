import numpy as np
import matplotlib.pyplot as plt

#Returns the raster plot and compute firing rates for the correspondong group of clusters
def raster_plot(spt_mat,trig,cluster_list='all',dmr=1,ftsize=22):
    # Decide cluster list
    if cluster_list=='all':
        cluster_list=spt_mat[:,0].astype(int)
    else:
        #cluster_list=[1,4,14,16,17,18,27,28,29,32,35,38,43,53,61,65,83,185,198]
        #cluster_list=[1,4,14,16,17,18,27,32,35,38,43]
        cluster_list=[6,14,19,27,46,47,58,59,61,71,75,81,82,94,100,104,156,175,176,178,182,190,191,204,205,207,209]

    #Conversion from bin to time
    fs=24414.0625
    first_t=np.amin(trig)/fs
    last_t=np.amax(trig)/fs

    gs=plt.GridSpec(40,20)
    ax1=plt.subplot(gs[0:6,0:7])
    N_clu=spt_mat.shape[0]
    N_clu_list=len(cluster_list)
    list_clu=np.zeros(N_clu)
    list_max=[]
    for clu_ind in range(N_clu):
        list_max.append(np.amax(spt_mat[clu_ind][1]))
        list_clu[clu_ind]=spt_mat[clu_ind][0][0][0]

    max_t=np.amax(list_max)
    fir_rate=[]
    # Generating raster plot and firing rate
    for clu_ind in range(N_clu_list):
        ind_neuron=np.where(list_clu==cluster_list[clu_ind])[0][0]

        fir_rate.append(np.sum(np.ones_like(spt_mat[ind_neuron][1][(spt_mat[ind_neuron][1]<=last_t) & (spt_mat[ind_neuron][1]>=first_t)])))
        plt.plot(spt_mat[ind_neuron][1][(spt_mat[ind_neuron][1]<=last_t) & (spt_mat[ind_neuron][1]>=first_t)],
                     clu_ind-1+np.ones_like(spt_mat[ind_neuron][1][(spt_mat[ind_neuron][1]<=last_t) & (spt_mat[ind_neuron][1]>=first_t)]),'|',color='k',alpha=0.1)

    plt.xlabel('Time (s)',fontsize=ftsize)
    plt.ylabel('Clusters',fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(np.arange(len(cluster_list)),cluster_list,fontsize=ftsize)


    ax2=plt.subplot(gs[0:6,7:9],sharey=ax1)

    plt.barh(np.arange(N_clu_list),np.array(fir_rate)/(last_t-first_t),color='#ff7f0e')
    plt.xlabel('Mean firing rate (Hz)',fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)

    return cluster_list
