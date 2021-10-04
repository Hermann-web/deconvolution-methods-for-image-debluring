import numpy as np
from scipy.optimize import minimize_scalar
from astropy.modeling import models, fitting
from astropy.io import fits
from scipy.linalg import toeplitz, hankel

def kronDecomp (P,*args):

    nargin = 1 + len(args)
    
    if (nargin < 2):
        print("Veuillez entrer le P et le Centre")
    if (nargin < 3):
        BC = zero

    #PSF
    im = fits.getdata("C:/Python37/pic.jpg")
    PSF = np.where(im == np.max(pic))
    
    center1= int(PSF[0])
    center2 = int(PSF[1])


    [U,S,V] = np.linalg.svd(P, full_matrices=True)

    if (S[2,2]/S[1,1] > np.sqrt(eps)):
        print("Attention, le PSF n'est pas séparable")
    
    J = list(U)  #transformation de tableau numpy en liste python
    G = list(V)  #transformation de tableau numpy en liste python

    minU = abs(min(J[:,0]))
    maxU = max(abs(J[:,0]))

    if minU == maxU :

        U = -U
        V = -V

    c = np.sqrt(S[1,1]*U[:,1])
    r = np.sqrt(S[1,1]*V[:,1])

    if BC == 'zero':
        Ar = build_Topelitz (r, center2)
        Ac = build_Toeplitz (r, center1)

    elif BC == 'reflexive':
        Ar = build_Topelitz (r, center2) + buildHank(r, center2)
        Ac = build_Toeplitz (r, center1) + buildHank(r, center1)

    elif BC == 'periodic':
        Ar = buildCirc (r, center2)
        Ac = buildCirc (r, center1)

    else :
        print("Erreur, condition de bord invalide")


    return (Ar, Ac)

def build_Topelitz (c, k):
    n = np.shape(c)
    col = np.zeros((n, 1), float)
    row = np.transpose(col)
    col[0:n-k,0] = c[k-1:n-1]
    row[0,0:k-1] = np.transpose(c[k-1:-2:1]) 

    T = toeplitz(col, row)

    return (T)

def buildCirc(c, k):
    n = np.shape(c)
    col = [c[k-1:n-1], c[0:k-1]]
    row = [np.transpose(c[k-1:-2:1]), np.transpose(c[n:-2:k+1])]   

    C = toeplitz(col, row)

    return (C)

def buildHank (c, k):
    n = np.shape(c)
    col = np.zeros((n, 1), float)
    col[0:n-k-1] = c[k:n-1]
    row = np.zeros((n, 1), float)
    row[n-k+1:n-1] = c[0:k-2] 

    H = hankel(col, row)

    return (H)
 
