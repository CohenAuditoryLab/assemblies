import numpy as np
from sklearn.decomposition import PCA
from sklearn.decomposition import FastICA
#Perform assembly detection in shuffled z-norm matrices. This function is called in the Monte-Carlo analysis
def assembly_detection_shuf(z_norm_mat,N_sig):
    N_clu=z_norm_mat.shape[0]
    N_bins=z_norm_mat.shape[1]

    pca=PCA()
    z_norm_proj=pca.fit(z_norm_mat.T)
    eig_vals=z_norm_proj.explained_variance_
    eig_vecs=z_norm_proj.components_
    sig_eig_vec=eig_vecs[0:N_sig]

    #PCA
    pca=PCA(n_components=sig_eig_vec.shape[0])
    z_norm_proj=pca.fit_transform(z_norm_mat.T)

    #ICA
    ica=FastICA(n_components=sig_eig_vec.shape[0])
    z_norm_trans=ica.fit(z_norm_proj)
    #rot_seg=np.matmul(z_norm_trans.components_,sig_eig_vec)
    rot_seg=ica.transform(sig_eig_vec.T).T
    for r in range(rot_seg.shape[0]):
        rot_seg[r]=rot_seg[r]/np.linalg.norm(rot_seg[r])
        am=np.argmax(np.abs(rot_seg[r]))
        if rot_seg[r,am]<0:
            rot_seg[r]=-rot_seg[r]

    return rot_seg.flatten()
