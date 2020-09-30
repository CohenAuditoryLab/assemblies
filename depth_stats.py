import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

def depth_stats(path_info):
    data=np.load('variance_var_'+str(0.005)+'.npy',allow_pickle=True)
    r_order=np.argsort(data[:,9])
    param_sorted=data[r_order,:]
    rot_seg=param_sorted[1,11]

    print(rot_seg.shape)
    #rot_seg_dmr2=param_sorted[1,11]
    cluster_list=param_sorted[0,10]

    info_rec=loadmat(path_info+'test_struct.mat')['a']['data'][0][0][0]

    cluster_names=info_rec[2][:,0]
    full_cluster_list=[]
    prefix=27
    for names in info_rec[2][:,0]:
        full_cluster_list.append(int(names[0][27:]))

    full_cluster_list=np.array(full_cluster_list)
    depth=[]
    waveform=[]
    cluster_list_check=[]
    for ind_clu,i in zip(full_cluster_list,range(full_cluster_list.shape[0])):
        if ind_clu in cluster_list:
            cluster_list_check.append(ind_clu)
            depth.append(info_rec[9][:,0][i])
            waveform.append(info_rec[10][i])




    depth=np.array(depth)

    waveform=np.array(waveform)

    #Normalization
    for i in range(waveform.shape[0]):
        waveform[i]=waveform[i]/np.amax(np.abs(waveform[i]))
    rot_seg[rot_seg<0]=0
    fig=plt.figure(figsize=(15,12))
    gs=plt.GridSpec(17,16)
    ftsize=8

    '''ax=plt.subplot(gs[0:4,4:8])
    plt.imshow(rot_seg.T,interpolation='None',aspect='auto',origin='lower left',cmap='cividis')
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    cbar=plt.colorbar()
    cbar.ax.tick_params(labelsize=4)'''
    #Depth plot
    '''plt.subplot(gs[0:4,0:4])
    plt.hist(depth[:])
    plt.xticks(fontsize=ftsize)
    plt.yticks(fontsize=ftsize)
    '''
    colors=['tab:blue', 'tab:orange', 'tab:green', 'tab:red']


    for a in range(param_sorted[0,0]):
        if a<2:
            plt.subplot(gs[0:4,a*4:(a+1)*4])
            plt.title('Assembly '+str(a+1),fontsize=ftsize)
        else:
            plt.subplot(gs[4:8,(a-2)*4:(a-1)*4])
            plt.title('Assembly '+str(a+1),fontsize=ftsize)
        h,_,_=plt.hist(depth[:],weights=rot_seg[a],color=colors[a])
        plt.vlines(np.average(depth[:],weights=rot_seg[a]),0,np.amax(h),color='k',ls='--',lw=2.)
        plt.xlabel('Depth cluster',fontsize=ftsize)
        plt.xticks(fontsize=ftsize)
        plt.yticks(fontsize=ftsize)

        if a<2:
            plt.subplot(gs[9:13,4*a:4*(a+1)])
            plt.title('Assembly '+str(a+1),fontsize=ftsize)
        else:
            plt.subplot(gs[13:17,4*(a-2):4*(a-1)])
            plt.title('Assembly '+str(a+1),fontsize=ftsize)
        for i in range(waveform.shape[0]):

            plt.plot(waveform[i,:],alpha=np.amax(rot_seg[a,i],0)+0.2,color=colors[a],lw=1)
            plt.xticks(fontsize=ftsize)
            plt.yticks(fontsize=ftsize)
            plt.grid(True)
        plt.plot(np.average(waveform,weights=rot_seg[a,:],axis=0),color='k',lw=2.5,label='weighted mean')
        plt.legend(fontsize=ftsize)

        plt.subplot(gs[9:17,8:16])
        plt.plot(np.average(waveform,weights=rot_seg[a,:],axis=0),color=colors[a],lw=3.0,label='Assembly '+str(a+1))
        plt.xticks(fontsize=ftsize)
        plt.yticks(fontsize=ftsize)
        plt.legend(fontsize=ftsize)
        plt.grid(True)

        plt.subplot(gs[0:8,8:16])
        if a==0:
            h_all,_,_=plt.hist(depth[:],color='tab:grey')
            plt.vlines(np.mean(depth[:]),0,np.amax(h_all),color='k',ls='--',lw=2.5,label='Non-weighted mean')
        plt.vlines(np.average(depth[:],weights=rot_seg[a]),0,np.amax(h_all),color=colors[a],ls='--',lw=2.5,label='Assembly '+str(a+1))
        plt.xticks(fontsize=ftsize)
        plt.xlabel('Depth cluster',fontsize=ftsize)
        plt.legend(fontsize=ftsize)
        plt.yticks(fontsize=ftsize)



    plt.tight_layout()
    plt.savefig('fig_waveform.pdf')


if __name__ == '__main__':
    path_info='../data_Lalitta/Cassius-190326/'
    depth_stats(path_info)
    #depth_stats("C:\Users\jhles\Desktop\work_penn\data_Lalitta\Cassius-190326\")
