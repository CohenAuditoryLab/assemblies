import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

def variance_explained_assembly_plot(monkey,col,color,time_window=0.01):

    ftsize=10
    variance_var=np.load('../../'+str(monkey)+'/'+str(monkey)+'_data_serial_mc_True_'+str(time_window)+'.npy',allow_pickle=True)
    gs=plt.GridSpec(24,10)
    #print(variance_var[0,5][0:1])

    vard=[]
    for arr,i in zip(variance_var[:,5],range(variance_var[:,5].shape[0])):
        if isinstance(arr, (np.ndarray, np.generic)):
            vard.append(variance_var[i,5][0:variance_var[i,0]])

    vard=np.array(vard)
    conc_vard=np.concatenate(vard,axis=0)

    plt.subplot(gs[0:4,4*col:4*(col+1)])
    plt.title('Variance explained by each assembly',fontsize=ftsize+2)
    plt.hist(100*conc_vard,bins=np.linspace(0,70,20),alpha=0.5,color=color,weights=100*(np.ones_like(conc_vard)/conc_vard.shape[0]))
    plt.axvline(x=np.mean(conc_vard)*100,ls='--',lw=3,label='Mean',color='tab:orange')
    plt.xlabel('% variance explained', fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.ylabel('% of datasets')
    plt.xlim([0,70])
    plt.ylim([0,100])
    plt.legend()


    N_assembly_max=4
    vardit=[[] for i in range(N_assembly_max)]

    for arr in vard:
        for na in range(arr.shape[0]):
            vardit[na].append(arr[na])


    for na in range(N_assembly_max):

        plt.subplot(gs[4*na+4:4*(na+1)+4,4*col:4*(col+1)])
        plt.title('Variance explained, assembly '+str(na+1),fontsize=ftsize+2)
        plt.hist(np.array(vardit[na])*100.,bins=np.linspace(0,70,20),alpha=0.5,color=color,weights=100*(np.ones_like(np.array(vardit[na]))/np.array(vardit[na]).shape[0]))
        plt.axvline(x=np.mean(np.array(vardit[na]))*100.,ls='--',lw=3,label='Mean',color='tab:orange')
        plt.xlabel('% Variance explained', fontsize=ftsize)
        plt.xticks(fontsize=ftsize)
        plt.yticks(fontsize=ftsize)
        plt.xlim([0,70])
        plt.ylim([0,100])
        plt.ylabel('% of datasets')
        plt.legend()

        plt.tight_layout()


if __name__ == '__main__':
    fig=plt.figure(figsize=(20,24))
    gs=plt.GridSpec(24,10)
    variance_explained_assembly_plot('cassius',0,'tab:blue',time_window=0.01)
    variance_explained_assembly_plot('miyagi',1,'tab:pink',time_window=0.01)
    fig.savefig('../../figures/fig_variance_decrease.pdf',bbox_inches='tight')
