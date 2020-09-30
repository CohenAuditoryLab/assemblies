import numpy as np
from math import comb


def word_collection(assembly_activity_ica_thresh,time_window,word_length,shuffle=False):

    N_tot=assembly_activity_ica_thresh.shape[1]
    N_assemblies=assembly_activity_ica_thresh.shape[0]
    if shuffle:
        for c in range(N_assemblies):
            perm=np.random.permutation(N_tot)
            assembly_activity_ica_thresh[c,:]=assembly_activity_ica_thresh[c,perm]

    N_words=int(N_tot/word_length)
    word_dict=[[[] for sw in range(word_length)] for a in range(N_assemblies)]
    ct=0

    # Collecting words
    for a in range(N_assemblies):
        for b in range(N_words):
            for sw in range(word_length):
                if (word_length*(b+1)+sw)<=N_words:
                    s=''.join(map(str,assembly_activity_ica_thresh[a,word_length*b+sw:word_length*(b+1)+sw].astype(int)))
                    s2=s.replace(' ', '')
                    word_dict[a][sw].append(s2)
                    s2=''
                    s=''
                    ct+=1
        print('Assembly '+str(a+1)+': done' )
    np.save('word_collection_shuffle_'+str(shuffle)+'.npy',np.array(word_dict))
