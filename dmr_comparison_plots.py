import matplotlib.pyplot as plt
import numpy as np

def dmr_comparison_plots(path,time_window=0.01):
    ftsize=10
    variance_var=np.load(path+'/variance_var_'+str(time_window)+'.npy',allow_pickle=True)
    r_order=np.argsort(variance_var[:,9])
    param_sorted=variance_var[r_order,:]

    fig=plt.figure(figsize=(20,18))
    gs=plt.GridSpec(20,16)
    ax=plt.subplot(gs[0:4,0:4])
    plt.title('Number of assemblies',fontsize=ftsize+2)
    x=np.arange(int(param_sorted.shape[0]/2))
    labels=[]
    for na in range(int(param_sorted.shape[0]/2)):
        labels.append(str(param_sorted[2*na,6])+';'+str(param_sorted[2*na,7]))

    width=0.35
    plt.bar(x-0.5*width,param_sorted[::2,0],color='tab:blue',width=0.35,label='DMR 1')
    plt.bar(x+0.5*width,param_sorted[1::2,0],color='tab:orange',width=width,label='DMR 2')
    ax.set_ylabel('Number of assemblies',fontsize=ftsize)
    ax.set_xticks(x)
    ax.set_xticklabels(labels,fontsize=ftsize-4)
    ax.legend()


    ax1=plt.subplot(gs[0:4,4:8])
    plt.title('Variance explained (%)',fontsize=ftsize+2)
    plt.bar(x-0.5*width,param_sorted[::2,2]*100,color='tab:blue',width=0.35,label='DMR 1')
    plt.bar(x+0.5*width,param_sorted[1::2,2]*100,color='tab:orange',width=width,label='DMR 2')
    ax1.set_ylabel('Variance explained (%)',fontsize=ftsize)
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels,fontsize=ftsize-4)
    ax1.legend()

    plt.subplot(gs[5:9,0:4])
    plt.title('All variance explained curves',fontsize=ftsize+2)
    cm_subsection = np.linspace(0, 1,int(param_sorted.shape[1]/2))
    colors = [ plt.cm.tab10(x) for x in cm_subsection ]
    for p in range(int(param_sorted.shape[1]/2)):
        x=np.arange(len(param_sorted[2*p,5]))+1
        plt.plot(x,param_sorted[2*p,5]*100.,lw=3,alpha=0.5,color=colors[p],label='DMR 1,'+str(str(variance_var[2*p,6])+';'+str(variance_var[2*p,7])))
        plt.plot(x,param_sorted[2*p+1,5]*100.,lw=3,alpha=0.5,ls='--',color=colors[p],label='DMR 2,'+str(str(variance_var[2*p,6])+';'+str(variance_var[2*p,7])))
    plt.xlabel('Dimensions',fontsize=ftsize)
    plt.ylabel('% variance explained',fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.legend()

    ax2=plt.subplot(gs[5:9,4:8])
    plt.title('Mean variance explained (%)',fontsize=ftsize+2)
    plt.bar(x-0.5*width,param_sorted[::2,2]*100/param_sorted[::2,0],color='tab:blue',width=0.35,label='DMR 1')
    plt.bar(x+0.5*width,param_sorted[1::2,2]*100/param_sorted[1::2,0],color='tab:orange',width=width,label='DMR 2')
    ax2.set_ylabel('Mean variance explained by the assemblies',fontsize=ftsize)
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels,fontsize=ftsize-4)
    ax2.legend()

    fig.tight_layout()
    fig.savefig('fig_dmr_comparison.pdf',bbox_inches='tight')

if __name__ == '__main__':
    dmr_comparison_plots('.')
