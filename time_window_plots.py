import matplotlib.pyplot as plt
import numpy as np
from math import *

def time_window_plots(path,array_tw):

    list_param_data=[]
    list_param_data_sorted=[]
    for t,i in zip(array_tw,np.arange(len(array_tw))):
        list_param_data.append(np.load(path+'/variance_var_'+str(t)+'.npy',allow_pickle=True))
        r_order=np.argsort(list_param_data[i][:,9])
        list_param_data_sorted.append(list_param_data[i][r_order,:])
    list_param_data_sorted=np.array(list_param_data_sorted)
    ftsize=14
    fig=plt.figure(figsize=(20,20))
    gs=plt.GridSpec(20,16)
    plt.subplot(gs[0:6,0:6])
    cm_subsection = np.linspace(0, 1,int(list_param_data_sorted.shape[1]))
    colors = [ plt.cm.tab10(x) for x in cm_subsection ]
    for d in range(list_param_data_sorted.shape[1]):
        if d==0:
            plt.plot(array_tw,list_param_data_sorted[:,d,0],'o-',alpha=0.4,color=colors[d],label='Samples',lw=2)
        else:
            plt.plot(array_tw,list_param_data_sorted[:,d,0],'o-',alpha=0.4,color=colors[d],lw=2)
    plt.errorbar(array_tw,np.mean(list_param_data_sorted[:,:,0],axis=1),yerr=np.sqrt(list(np.var(list_param_data_sorted[:,:,0],axis=1))),fmt='o-',color='k',label='Mean',lw=2.5)
    plt.xlabel('Time window (seconds)',fontsize=ftsize)
    plt.ylabel('Number of assemblies',fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.grid(True)
    plt.legend()
    plt.ylim([0,10])



    plt.subplot(gs[0:6,6:12])
    cm_subsection = np.linspace(0, 1,int(list_param_data_sorted.shape[1]))
    colors = [ plt.cm.tab10(x) for x in cm_subsection ]
    for d in range(list_param_data_sorted.shape[1]):
        if d==0:
            plt.plot(array_tw,list_param_data_sorted[:,d,2]*100,'o-',alpha=0.4,color=colors[d],label='Samples',lw=2)
        else:
            plt.plot(array_tw,list_param_data_sorted[:,d,2]*100,'o-',alpha=0.4,color=colors[d],lw=2)

    plt.errorbar(array_tw,np.mean(list_param_data_sorted[:,:,2]*100,axis=1),yerr=np.sqrt(list(np.var(list_param_data_sorted[:,:,2]*100,axis=1))),fmt='o-',color='k',label='Mean',lw=2.5)
    plt.xlabel('Time window (seconds)',fontsize=ftsize)
    plt.ylabel('Variance explained (%)',fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.grid(True)
    plt.legend()
    plt.ylim([0,100])

    plt.subplot(gs[6:12,0:6])
    cm_subsection = np.linspace(0, 1,int(list_param_data_sorted.shape[1]))
    colors = [ plt.cm.tab10(x) for x in cm_subsection ]
    for d in range(list_param_data_sorted.shape[1]):
        if d==0:
            plt.plot(array_tw,list_param_data_sorted[:,d,2]*100./list_param_data_sorted[:,d,0],'o-',alpha=0.4,color=colors[d],label='Samples',lw=2)
        else:
            plt.plot(array_tw,list_param_data_sorted[:,d,2]*100./list_param_data_sorted[:,d,0],'o-',alpha=0.4,color=colors[d],lw=2)

    plt.errorbar(array_tw,np.mean(list_param_data_sorted[:,:,2]*100./list_param_data_sorted[:,:,0],axis=1),yerr=np.sqrt(list(np.var(list_param_data_sorted[:,:,2]*100/list_param_data_sorted[:,:,0],axis=1))),fmt='o-',color='k',lw=2.5,label='Mean')
    plt.xlabel('Time window (seconds)',fontsize=ftsize)
    plt.ylabel('Mean variance explained per assembly (%)',fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.grid(True)
    plt.legend()

    plt.subplot(gs[6:9,6:9])
    plt.title('Time window: '+str(array_tw[0])+' seconds',fontsize=ftsize)
    cm_subsection = np.linspace(0, 1,int(list_param_data_sorted.shape[1]/2))
    colors = [ plt.cm.tab10(x) for x in cm_subsection ]
    for p in range(int(list_param_data_sorted.shape[1]/2)):
        x=np.arange(len(list_param_data_sorted[0,2*p,5]))+1
        plt.plot(x,list_param_data_sorted[0,2*p,5]*100,lw=3,alpha=0.5,color=colors[p],label='DMR 1,'+str(list_param_data_sorted[0,2*p,6])+';'+str(list_param_data_sorted[0,2*p,7]))
        plt.plot(x,list_param_data_sorted[0,2*p+1,5]*100,lw=3,alpha=0.5,ls='--',color=colors[p],label='DMR 2,'+str(list_param_data_sorted[0,2*p,6])+';'+str(list_param_data_sorted[0,2*p,7]))
    plt.xlabel('Dimensions',fontsize=ftsize)
    plt.ylabel('% variance explained',fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.ylim([0,40])
    #plt.legend()
    plt.subplot(gs[6:9,9:12])
    plt.title('Time window: '+str(array_tw[2])+' seconds',fontsize=ftsize)
    cm_subsection = np.linspace(0, 1,int(list_param_data_sorted.shape[1]/2))
    colors = [ plt.cm.tab10(x) for x in cm_subsection ]
    for p in range(int(list_param_data_sorted.shape[1]/2)):
        x=np.arange(len(list_param_data_sorted[2,2*p,5]))+1
        plt.plot(x,list_param_data_sorted[2,2*p,5]*100.,lw=3,alpha=0.5,color=colors[p],label='DMR 1,'+str(list_param_data_sorted[2,2*p,6])+';'+str(list_param_data_sorted[2,2*p,7]))
        plt.plot(x,list_param_data_sorted[2,2*p+1,5]*100.,lw=3,alpha=0.5,ls='--',color=colors[p],label='DMR 2,'+str(list_param_data_sorted[2,2*p,6])+';'+str(list_param_data_sorted[2,2*p,7]))
    plt.xlabel('Dimensions',fontsize=ftsize)
    plt.ylabel('% variance explained',fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.ylim([0,40])

    plt.subplot(gs[9:12,6:9])
    plt.title('Time window: '+str(array_tw[3])+' seconds',fontsize=ftsize)
    cm_subsection = np.linspace(0, 1,int(list_param_data_sorted.shape[1]/2))
    colors = [ plt.cm.tab10(x) for x in cm_subsection ]
    for p in range(int(list_param_data_sorted.shape[1]/2)):
        x=np.arange(len(list_param_data_sorted[3,2*p,5]))+1
        plt.plot(x,list_param_data_sorted[3,2*p,5]*100.,lw=3,alpha=0.5,color=colors[p],label='DMR 1,'+str(list_param_data_sorted[3,2*p,6])+';'+str(list_param_data_sorted[3,2*p,7]))
        plt.plot(x,list_param_data_sorted[3,2*p+1,5]*100.,lw=3,alpha=0.5,ls='--',color=colors[p],label='DMR 2,'+str(list_param_data_sorted[3,2*p,6])+';'+str(list_param_data_sorted[3,2*p,7]))
    plt.xlabel('Dimensions',fontsize=ftsize)
    plt.ylabel('% variance explained',fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.ylim([0,40])

    plt.subplot(gs[9:12,9:12])
    plt.title('Time window: '+str(array_tw[4])+' seconds',fontsize=ftsize)
    cm_subsection = np.linspace(0, 1,int(list_param_data_sorted.shape[1]/2))
    colors = [ plt.cm.tab10(x) for x in cm_subsection ]
    for p in range(int(list_param_data_sorted.shape[1]/2)):
        x=np.arange(len(list_param_data_sorted[4,2*p,5]))+1
        plt.plot(x,list_param_data_sorted[4,2*p,5]*100.,lw=3,alpha=0.5,color=colors[p],label='DMR 1,'+str(list_param_data_sorted[4,2*p,6])+';'+str(list_param_data_sorted[4,2*p,7]))
        plt.plot(x,list_param_data_sorted[4,2*p+1,5]*100.,lw=3,alpha=0.5,ls='--',color=colors[p],label='DMR 2,'+str(list_param_data_sorted[4,2*p,6])+';'+str(list_param_data_sorted[4,2*p,7]))
    plt.xlabel('Dimensions',fontsize=ftsize)
    plt.ylabel('% variance explained',fontsize=ftsize)
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    plt.ylim([0,40])


    fig.tight_layout()
    fig.savefig('fig_time_window.pdf',bbox_inches='tight')

    #plt.plot(list_param_data_sorted[:][a,0]
if __name__ == '__main__':
    time_window_plots('.',[0.005,0.01,0.02,0.05,0.1])
