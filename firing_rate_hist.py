import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

def firing_rate_hist(monkey,col,color,time_window=0.01):

    variance_var=np.load('../../'+str(monkey)+'/'+str(monkey)+'_data_serial_mc_True_'+str(time_window)+'.npy',allow_pickle=True)
    gs=plt.GridSpec(20,20)
    ftsize=12
    print(variance_var[:,13][0])
    '''
    plt.subplot(gs[1:5,4*col:4*(col+1)])
    plt.title('Firing rate, assembly 1',fontsize=ftsize+2)
    plt.hist(variance_var[13],alpha=0.5,color=color)#,weights=100*(np.ones_like(variance_var[:,13][0])/variance_var[:,13][0].shape[0]))
    plt.axvline(x=np.mean(variance_var[:,13][0]),ls='--',lw=3,label='Mean',color='tab:orange')
    plt.xlabel('Firing rate (Hz)',fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.ylabel('% of datasets')
    #plt.ylim([0,50])
    #plt.xlim([0,20])
    plt.legend()
    plt.tight_layout()
    '''

if __name__ == '__main__':

    fig=plt.figure(figsize=(20,18))
    firing_rate_hist('cassius',0,'tab:blue',time_window=0.01)
    fig.savefig('../../figures/fig_firing_rate_assemblies.pdf',bbox_inches='tight')
