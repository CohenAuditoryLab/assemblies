import matplotlib.pyplot as plt
import numpy as np

def variance_plots(monkey,color,col,time_window=0.01):
    ftsize=6
    #variance_var=np.load(path+'/variance_var_'+str(time_window)+'.npy',allow_pickle=True)
    variance_var=np.load('../../'+str(monkey)+'/'+str(monkey)+'_data_serial_'+str(time_window)+'.npy',allow_pickle=True)
    #fig=plt.figure(figsize=(20,18))
    gs=plt.GridSpec(20,9)
    #plt.suptitle(str(monkey),color=color)
    # Histogram number of assemblies
    plt.subplot(gs[1:5,4*col:4*(col+1)])
    plt.title('Number of neurons',fontsize=ftsize+2)
    plt.hist(variance_var[:,3],bins=np.arange(40)-0.5,alpha=0.5,color=color,weights=100*(np.ones_like(variance_var[:,3])/variance_var[:,3].shape[0]))
    plt.axvline(x=np.mean(variance_var[:,3]),ls='--',lw=3,label='Mean',color='tab:orange')
    plt.xlabel('Number of assemblies',fontsize=ftsize)
    plt.xticks(np.arange(40),fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.xlabel('Number of neurons')
    plt.ylabel('% of datasets')
    plt.ylim([0,50])
    plt.xlim([0,40])
    plt.legend()


    plt.subplot(gs[6:10,4*col:4*(col+1)])
    plt.title('Number of assemblies',fontsize=ftsize+2)
    plt.hist(variance_var[:,0],bins=np.arange(6)-0.5,alpha=0.5,color=color,weights=100*(np.ones_like(variance_var[:,0])/variance_var[:,0].shape[0]))
    plt.axvline(x=np.mean(variance_var[:,0]),ls='--',lw=3,label='Mean',color='tab:orange')
    plt.xlabel('Number of assemblies',fontsize=ftsize)
    plt.xticks(np.arange(11),fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.xlabel('Number of assemblies')
    plt.ylabel('% of datasets')
    plt.ylim([0,50])
    plt.xlim([0,7])
    plt.legend()

    # Histogram ratio assemblies/clusters
    plt.subplot(gs[11:15,4*col:4*(col+1)])
    plt.title('Ratio assembly/cluster',fontsize=ftsize+2)
    plt.hist(variance_var[:,0]/variance_var[:,3],bins=20,alpha=0.5,color=color,weights=100*(np.ones_like(variance_var[:,0])/variance_var[:,0].shape[0]))
    plt.axvline(x=np.mean(variance_var[:,0]/variance_var[:,3]),ls='--',lw=3,label='Mean',color='tab:orange')
    plt.xlabel('Ratio assemblies/clusters',fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.ylabel('% of datasets')
    plt.ylim([0,50])
    plt.xlim([0,0.6])
    plt.legend()

    # Histogram of variance explained
    plt.subplot(gs[16:20,4*col:4*(col+1)])
    plt.title('Variance explained ',fontsize=ftsize+2)
    plt.hist(variance_var[:,2]*100,bins=20,alpha=0.5,color=color,weights=100*(np.ones_like(variance_var[:,2])/variance_var[:,2].shape[0]))
    plt.axvline(x=np.mean(variance_var[:,2])*100,ls='--',lw=3,label='Mean',color='tab:orange')
    plt.xlabel('% cumulative variance explained by assemblies',fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    #plt.ylabel('% of datasets')
    plt.ylim([0,50])
    plt.xlim([0,70])
    plt.legend()
    if monkey=='cassius':
        plt.text(15,250,'Cassius, number of datasets: '+str(variance_var[:,0].shape[0]),fontsize=15,color=color)
    else:
        plt.text(15,250,'MrMiyagi, number of datasets: '+str(variance_var[:,0].shape[0]),fontsize=15,color=color)
    '''
    #Best fit pyplot
    def power_law(x,alpha):
        return x**(alpha)

    plt.subplot(gs[5:9,4:8])
    plt.title('Best fit',fontsize=ftsize+2)
    best_fit_ind=np.argmin(variance_var[:,4])
    x=np.arange(len(variance_var[best_fit_ind,5]))+1
    y_fit=np.poly1d(variance_var[best_fit_ind,1])(x)
    plt.plot(x,variance_var[best_fit_ind,5],ls='--',lw=4,label='Data')
    plt.plot(x,y_fit,'*',markersize=10,label='Polynomial Fit (deg=3)')
    plt.xlabel('Dimensions',fontsize=ftsize)
    plt.ylabel('% variance explained',fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.legend()

    plt.subplot(gs[5:9,0:4])
    plt.title('All variance explained curves',fontsize=ftsize+2)
    for p in range(variance_var.shape[0]):
        x=np.arange(len(variance_var[p,5]))+1
        plt.plot(x,variance_var[p,5]*100.,lw=2.5,alpha=0.5)
    plt.xlabel('Dimensions',fontsize=ftsize)
    plt.ylabel('% variance explained',fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)


    plt.subplot(gs[5:9,8:12])
    plt.title('Degree 3 coefficient',fontsize=ftsize+2)
    z_param=np.array(variance_var[:,1])
    N_degree=4
    z=[[] for i in range(N_degree)]
    for p in range(z_param.shape[0]):
        for i in range(N_degree):
            z[i].append(z_param[p][i])
    plt.hist(z[0],bins=30,alpha=0.5)
    plt.axvline(x=np.mean(z[0]),ls='--',lw=3,label='Mean',color='tab:orange')
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.legend()

    plt.subplot(gs[10:14,0:4])
    plt.title('Degree 2 coefficient',fontsize=ftsize+2)
    plt.hist(z[1],bins=30,alpha=0.5)
    plt.axvline(x=np.mean(z[1]),ls='--',lw=3,label='Mean',color='tab:orange')
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.legend()

    plt.subplot(gs[10:14,4:8])
    plt.title('Degree 1 coefficient',fontsize=ftsize+2)
    plt.hist(z[2],bins=30,alpha=0.5)
    plt.axvline(x=np.mean(z[2]),ls='--',lw=3,label='Mean',color='tab:orange')
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.legend()

    plt.subplot(gs[10:14,8:12])
    plt.title('Degree 0 coefficient',fontsize=ftsize+2)
    plt.hist(z[3],bins=30,alpha=0.5)
    plt.axvline(x=np.mean(z[3]),ls='--',lw=3,label='Mean',color='tab:orange')
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.legend()
    '''

    #plt.tight_layout()
    #plt.show()

if __name__ == '__main__':
    fig=plt.figure(figsize=(20,18))
    gs=plt.GridSpec(20,9)
    variance_plots('cassius','tab:blue',0,0.01)
    variance_plots('miyagi','tab:pink',1,0.01)

    plt.tight_layout()
    #plt.show()
    fig.savefig('../../figures/fig_general_stat.pdf',bbox_inches='tight')
