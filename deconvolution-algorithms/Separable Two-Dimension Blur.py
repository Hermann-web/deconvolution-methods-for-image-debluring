#Separable Two-dimensional Blur

import numpy as np
from scipy.optimize import minimize_scalar
from astropy.modeling import models, fitting
from astropy.io import fits


'''Trouver le PSF
im = fits.getdata("C:/Python37/pic.jpg")
PSF = np.where(im == np.max(pic))'''

''' Trouver le centre du PSF
xc = int(cents[1])
yc = int(cents[0])

center = [xc,yc]'''

def tsvd_sep (B, PSF, *args):
    
    nargin = 2 + len(args)
    
    if (nargin < 3):
        print("Veuillez entrer Center")
    if (nargin < 4):
        tol = []
    if (nargin < 5):
        BC = 'zero'

    [Ar, Ac] = kronDecomp (PSF, center, BC)
    [Ur,Sr,Vr] = np.linalg.svd(Ar, full_matrices=True)
    [Uc,Sc,Vc] = np.linalg.svd(Ac, full_matrices=True)

    bhat = np.transpose(Uc)*B*Ur
    bhat = bhat.flatten()

    S = np.kron(np.diag(np.diag(Sr)), np.diag(np.diag(Sc)))

    #find tol if not given
    if isalpha(tol) or tol==[]:
        tol = gcv_tsvd(s,bhat[:])

    phi = []
    for i in range (len(s)):
        k = abs(s[i])
        if k >= tol:
            phi.append(k)
            
    sfilt = np.zeros(np.shape(phi))
    for i in range (len(phi)):
        j = phi[i]/s[i]
        sfilt.append(j)

    f = bhat * sflit
    Bhat = np.reshape(f, np.shaope(B))
    x = Vc*Bhat*np.transpose(Vr)

    return (x, tol)
