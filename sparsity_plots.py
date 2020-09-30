import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

def sparsity_plots(monkey,col,color,time_window=0.01):
    ftsize=10
    variance_var=np.load('../../'+str(monkey)+'/'+str(monkey)+'_data_serial_mc_True_'+str(time_window)+'.npy',allow_pickle=True)
    gs=plt.GridSpec(24,10)
    spar=[]
    for arr in variance_var[:,14]:
        if isinstance(arr, (np.ndarray, np.generic)):
            spar.append(arr)
    spar=np.array(spar)
    conc_spar=np.concatenate(spar,axis=0)

    plt.subplot(gs[0:4,4*col:4*(col+1)])
    plt.title('Sparsity',fontsize=ftsize+2)
    plt.hist(conc_spar,bins=np.linspace(0,1,20),alpha=0.5,color=color,weights=100*(np.ones_like(conc_spar)/conc_spar.shape[0]))
    plt.axvline(x=np.mean(conc_spar),ls='--',lw=3,label='Mean',color='tab:orange')
    plt.xlabel('Sparsity', fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.ylabel('% of datasets')
    plt.xlim([0,1])
    plt.ylim([0,50])
    plt.legend()


    N_assembly_max=4
    sparit=[[] for i in range(N_assembly_max)]



    for arr in spar:
        for na in range(arr.shape[0]):
            sparit[na].append(arr[na])


    for na in range(N_assembly_max):

        plt.subplot(gs[4*na+4:4*(na+1)+4,4*col:4*(col+1)])
        plt.title('Sparsity, assembly '+str(na+1),fontsize=ftsize+2)
        plt.hist(np.array(sparit[na]),bins=np.linspace(0,1,20),alpha=0.5,color=color,weights=100*(np.ones_like(np.array(sparit[na]))/np.array(sparit[na]).shape[0]))
        plt.axvline(x=np.mean(np.array(sparit[na])),ls='--',lw=3,label='Mean',color='tab:orange')
        plt.xlabel('Sparsity', fontsize=ftsize)
        plt.xticks(fontsize=ftsize)
        plt.yticks(fontsize=ftsize)
        plt.ylabel('% of datasets')
        plt.xlim([0,1])
        plt.ylim([0,50])
        plt.legend()

        plt.tight_layout()





if __name__ == '__main__':

    fig=plt.figure(figsize=(20,24))
    gs=plt.GridSpec(24,10)
    sparsity_plots('cassius',0,'tab:blue',time_window=0.01)
    sparsity_plots('miyagi',1,'tab:pink',time_window=0.01)
    fig.savefig('../../figures/fig_sparsity.pdf',bbox_inches='tight')
