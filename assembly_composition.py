import numpy as np

def assembly_composition(rot_seg,sd,m):
 
    for v in range(rot_seg.shape[0]):
        for w in range(rot_seg.shape[1]):
            if rot_seg[v,w]>=m+0.5*sd or rot_seg[v,w]<=-m-0.5*sd:
                rot_seg[v,w]=1
            else:
              rot_seg[v,w]=0
    return rot_seg
