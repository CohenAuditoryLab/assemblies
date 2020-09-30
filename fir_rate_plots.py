import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

def fir_rate_plots(monkey,time_window=0.01):
    time=300
    #data=np.load('variance_var_serial'+str(0.005)+'.npy',allow_pickle=True)
    data=np.load('../../'+str(monkey)+'/'+str(monkey)+'_data_serial_'+str(time_window)+'.npy',allow_pickle=True)
    r_order=np.argsort(data[:,9])
    param_sorted=data[r_order,:]
    fir_rate_arr=param_sorted[:,12]
    fir_rate_assemblies_arr=param_sorted[:,13]
    print(fir_rate_assemblies_arr)
    rot_seg_arr=param_sorted[:,11]
    labels=[]
    for na in range(int(param_sorted.shape[0]/2)):
        labels.append(str(param_sorted[2*na,6])+';'+str(param_sorted[2*na,7]))
    #print(fir_rate_arr[2].shape)
    #print(rot_seg_arr[2].shape)
    N_data_set=int(param_sorted.shape[0]/2)
    fig=plt.figure(figsize=(10,15))
    # Weighted firing rates
    for d in range(N_data_set):
        ax=plt.subplot(321+d)
        plt.title(str(labels[d]))
        x=np.arange(int(rot_seg_arr[2*d].shape[0]))
        width=0.35
        rot_seg_arr[2*d][rot_seg_arr[2*d]<0]=0
        rot_seg_arr[2*d+1][rot_seg_arr[2*d+1]<0]=0
        bars1=[]
        bars2=[]
        for a in range(rot_seg_arr[2*d].shape[0]):
            #bars1.append(np.average(fir_rate_arr[2*d],weights=rot_seg_arr[2*d][a])/300)
            bars1.append(fir_rate_assemblies_arr[2*d][a]/300)
        for a in range(rot_seg_arr[2*d+1].shape[0]):
            #bars2.append(np.average(fir_rate_arr[2*d+1],weights=rot_seg_arr[2*d+1][a])/300)
            bars2.append(fir_rate_assemblies_arr[2*d+1][a]/300)

        plt.bar(x-0.5*width,bars1,color='tab:blue',width=0.35,label='DMR 1')
        plt.bar(x+0.5*width,bars2,color='tab:orange',width=0.35,label='DMR 2')
        #ax.set_xticklabels('Assemblies',fontsize=ftsize-4)
        plt.legend()
        plt.xlabel('Assemblies')
        plt.ylabel('Firing rate assemblies (Hz)')
        plt.xticks(x,x+1)
        plt.ylim([0,4])
    plt.tight_layout()
    plt.savefig('fig_fir_rate_2.pdf')
    #np.average(fir_rate_arr,weights=rot_seg_arr[])


if __name__ == '__main__':
    fir_rate_plots()
