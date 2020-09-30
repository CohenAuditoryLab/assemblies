import numpy as np
import matplotlib.pyplot as plt


def firing_rate_assemblies(assembly_activity_ica_thresh):
    fir_rate_assemblies=np.sum(assembly_activity_ica_thresh,axis=1)
    return fir_rate_assemblies
