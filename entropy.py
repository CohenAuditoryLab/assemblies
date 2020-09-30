import numpy as np
import matplotlib.pyplot as plt

def entropy():
    word_collect=np.load('word_collection_shuffle_True.npy',allow_pickle=True)
    N_assemblies=word_collect.shape[0]
    word_length=word_collect.shape[1]
    entropy_arr=np.zeros((N_assemblies,word_length))
    print(word_collect[0,0])
    for a in range(N_assemblies):
        for b in range(word_length):
            prob,_,_=plt.hist(word_collect[a,b],bins=len(set(word_collect[a,b])),weights=np.ones(len(word_collect[a,b]))/len(word_collect[a,b]))
            prob=prob[prob!=0]
            print(prob)
            entropy=-np.dot(prob,np.log2(prob))
            entropy_arr[a,b]=entropy
    print(entropy_arr)

if __name__ == '__main__':
    entropy()
