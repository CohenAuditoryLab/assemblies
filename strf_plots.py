import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import scipy.spatial.distance


def strf_similarity(strf1,strf2):
    p_cc=np.corrcoef(strf1.flatten(),strf2.flatten())[0,1]
    return p_cc

def clu_assembly_strf_comput(param_sorted,procnum,time_window):
    sim_res=[[] for n in range(param_sorted[procnum,0])]

    for n in range(param_sorted[procnum,0]):
        file_assembly='STRF_'+str(param_sorted[procnum,7])+'_'+str(param_sorted[procnum,6])+'_'+str(param_sorted[procnum,8])+'_assembly_'+str(n+1)+'_'+str(int(1000*time_window))+'.mat'
        path_assembly='./matlab_strf/strfs/'
        strf_assembly=scipy.io.loadmat(path_assembly+file_assembly)['STRF1s']

        for c in param_sorted[procnum,10]:
            file_cluster='STRF_'+str(param_sorted[procnum,7])+'_'+str(param_sorted[procnum,6])+'_'+str(param_sorted[procnum,8])+'_'+str(c)+'.mat'
            path_cluster='./matlab_strf/strfs/'
            strf_cluster=scipy.io.loadmat(path_cluster+file_cluster)['STRF1s']
            sim_res[n].append(strf_similarity(strf_assembly,strf_cluster))


    sim_res=np.array(sim_res)

    return sim_res

def assembly_strf_contr(param_sorted,ind):
    gs=plt.GridSpec(20,20)
    res_sim=[]
    res_sim.append(clu_assembly_strf_comput(param_sorted,2*ind,0.005))
    res_sim.append(clu_assembly_strf_comput(param_sorted,2*ind+1,0.005))
    distance_res=[]

    ftsize=8
    cluster_list=param_sorted[2*ind,10]
    N_dmr=2

    for d in range(N_dmr):
        if ind%2==0:
            ax=plt.subplot(gs[int(6*(ind/2)+3*d):int(6*(ind/2)+3*(d+1)),0:3])
        else:
            ax=plt.subplot(gs[int(6*((ind-1)/2)+3*d):int(6*((ind-1)/2)+3*(d+1)),6:9])
        plt.imshow(np.transpose(param_sorted[2*ind+d,11]),origin='lower left',interpolation=None,aspect='auto',cmap='cividis')
        cbar=plt.colorbar()
        cbar.ax.tick_params(labelsize=4)
        plt.xlabel('Assemblies',fontsize=ftsize)
        plt.ylabel('Neurons',fontsize=ftsize)
        plt.xticks(fontsize=ftsize)
        plt.yticks(np.arange(len(cluster_list)),cluster_list,fontsize=ftsize)

        if ind%2==0:
            ax1=plt.subplot(gs[int(6*(ind/2)+3*d):int(6*(ind/2)+3*(d+1)),3:6])
        else:
            ax1=plt.subplot(gs[int(6*((ind-1)/2)+3*d):int(6*((ind-1)/2)+3*(d+1)),9:12])
        plt.imshow(np.transpose(res_sim[d]),origin='lower left',interpolation=None,aspect='auto',cmap='cividis')
        plt.xticks(fontsize=ftsize)
        plt.xlabel('Assemblies',fontsize=ftsize)
        plt.ylabel('Neurons',fontsize=ftsize)
        plt.yticks(np.arange(len(cluster_list)),cluster_list,fontsize=ftsize)
        cbar1=plt.colorbar()
        cbar1.ax.tick_params(labelsize=4)
    for d in range(N_dmr):
        for n in range(param_sorted[2*ind,0]):
            distance_res.append(scipy.spatial.distance.cosine(param_sorted[2*ind+d,11][n],res_sim[d][n]))

    return distance_res


def all_plots(param_sorted):
    ftsize=8
    fig=plt.figure(figsize=(20,15))
    gs=plt.GridSpec(20,20)
    labels=[]
    res_distance=[]
    for na in range(int(param_sorted.shape[0]/2)):
        labels.append(str(param_sorted[2*na,6])+';'+str(param_sorted[2*na,7]))
    for p in range(int(param_sorted.shape[0]/2)):
        #plt.suptitle(labels[p], fontsize=ftsize+2)
        res_distance.append(assembly_strf_contr(param_sorted,p))
    plt.subplot(gs[12:18,6:12])
    plt.hist(sum(res_distance,[]),width=0.05)
    plt.xlabel('Cosine distance',fontsize=ftsize)
    print(np.array(res_distance).flatten())


    fig.tight_layout()
    fig.savefig('fig_strfs.pdf',bbox_inches='tight')



if __name__ == '__main__':
    data=np.load('variance_var_'+str(0.005)+'.npy',allow_pickle=True)
    r_order=np.argsort(data[:,9])
    param_sorted=data[r_order,:]
    all_plots(param_sorted)
