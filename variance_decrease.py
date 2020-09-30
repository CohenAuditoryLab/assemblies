import numpy as np
from sklearn.decomposition import PCA
from scipy.optimize import curve_fit

def variance_decrease(path,dmr,z_norm_mat,N_sig):
    N_clu=z_norm_mat.shape[0]
    N_bins=z_norm_mat.shape[1]

    pca=PCA()
    z_norm_proj=pca.fit(z_norm_mat.T)
    var_decrease=pca.explained_variance_ratio_
    variance_explained_N_sig=sum(var_decrease[0:N_sig])
    #print('Variance explained by significant components from'+str(path)+', dmr '+str(dmr)+': '+str(round(variance_explained_N_sig*100,2))+'%')

    def power_law(x,alpha):
        return x**(alpha)
    alpha, pcov = curve_fit(power_law, np.arange(N_clu)+1, var_decrease)
    #print('Alpha value from'+str(path)+', dmr'+str(dmr)+': '+str(round(alpha[0],2)))

    z = np.polyfit(np.arange(N_clu)+1, var_decrease, 3)
    p=np.poly1d(z)
    yfit=p(np.arange(N_clu)+1)                       #power_law(np.arange(N_clu)+1,alpha[0])
    euc_norm=np.linalg.norm(yfit-var_decrease)
    #print(euc_norm)
    return z,variance_explained_N_sig,euc_norm,var_decrease
