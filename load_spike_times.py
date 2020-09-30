import os
import scipy.io

# Function to load the spike times of each clusters
def load_spike_times(path):
    path_spikes=path+'/spike_times_good_clust.mat'
    if os.path.exists(path_spikes):
        spt_mat = scipy.io.loadmat(path_spikes)
        return spt_mat['spikeTimesGoodClust'],path_spikes
    else:
        print("Sorry, this folder doesn't exist, try another one")
        return
