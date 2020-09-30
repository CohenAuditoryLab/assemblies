import numpy as np
#Project z_norm_mat onto the subspace spanned by the siginificant component obtained with PCA or ICA
def projected_activity(z_norm_mat,sig_eig_vec,rot_seg_thresh):
    N_assembly=sig_eig_vec.shape[0]
    N_bins=z_norm_mat.shape[1]
    #Activity projected onto the subspace spanned by the significant PCA components
    assembly_activity_pca=np.zeros((N_assembly,N_bins))
    #Activity projected onto the subspace spanned by the significant ICA components
    assembly_activity_ica=np.zeros((N_assembly,N_bins))

    for a in range(N_assembly):
        assembly_pattern_pca=np.outer(sig_eig_vec[a,:],sig_eig_vec[a,:])
        np.fill_diagonal(assembly_pattern_pca, 0)
        assembly_pattern_ica=np.outer(rot_seg_thresh[a,:],rot_seg_thresh[a,:])
        np.fill_diagonal(assembly_pattern_ica, 0)
        for b in range(N_bins):
            proj_pca=np.matmul(z_norm_mat[:,b].T,assembly_pattern_pca)
            assembly_activity_pca[a,b]=np.matmul(proj_pca,z_norm_mat[:,b])
            proj_ica=np.matmul(z_norm_mat[:,b].T,assembly_pattern_ica)
            assembly_activity_ica[a,b]=np.matmul(proj_ica,z_norm_mat[:,b])
    return assembly_activity_pca,assembly_activity_ica
